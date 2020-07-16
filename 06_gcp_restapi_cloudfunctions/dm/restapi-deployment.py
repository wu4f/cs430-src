import google.auth
from googleapiclient import discovery
from googleapiclient.errors import HttpError
from google.cloud import storage
import time
import os
import zipfile
import httplib2

def wait_on_operation(opname, deployment_api, project_id):
    while True:
        time.sleep(1)
        print('.', end="", flush=True)
        op_status = deployment_api.operations().get(
            project=project_id,
            operation=op_name).execute()['status']
        if op_status == 'DONE':
            break
    return True

project_name = os.environ['GOOGLE_CLOUD_PROJECT']
location_name = 'us-central1'
deployment_name = f"{project_name}-restapi"
service_account = f"guestbook@{project_name}.iam.gserviceaccount.com"

credentials, project_id = google.auth.default()
deployment_api = discovery.build('deploymentmanager', 'v2', credentials=credentials)

#url_of_fn = upload_cloud_function('..', 'us-central1')
with zipfile.ZipFile('./function.zip', 'w') as z:
    z.write('../main.py', 'main.py')
    z.write('../requirements.txt', 'requirements.txt')
    for dir_path, subdir_paths, f_names in os.walk('../gbmodel'):
        for f in f_names:
            file_path = dir_path + '/' + f
            arc_path = file_path.replace('../', '')
            z.write(file_path, arcname=arc_path)
try:
    # Build api object
    cf_api = discovery.build('cloudfunctions', 'v1', credentials=credentials)
    parent = f'projects/{project_name}/locations/{location_name}'
    # Generate upload URL
    upload_url = cf_api.projects().locations().functions().generateUploadUrl(parent=parent).execute()['uploadUrl']
    # Make Http object
    h = httplib2.Http()
    # Upload to url
    headers = {'Content-Type': 'application/zip',
               'x-goog-content-length-range': '0,104857600'}
    with open('./function.zip', 'rb') as f:
        h.request(upload_url, method='PUT', headers=headers, body=f)
    # Return signed url for creating cloud function
    print(f'Upload URL is: {upload_url}')
finally:
    # Delete zip
    os.remove('./function.zip')

restapi_yaml = f'''
resources:
- type: gcp-types/cloudfunctions-v1:projects.locations.functions
  name: entries
  properties:
    function: entries
    parent: projects/{project_name}/locations/{location_name}
    sourceUploadUrl: {upload_url}
    entryPoint: entries
    runtime: python37
    httpsTrigger: {{}}
    serviceAccountEmail: guestbook@{project_name}.iam.gserviceaccount.com
- name: entries-iam-binding-func-allUsers
  type: gcp-types/cloudfunctions-v1:virtual.projects.locations.functions.iamMemberBinding
  properties:
    resource: $(ref.entries.name)
    role: roles/cloudfunctions.invoker
    member: allUsers
'''

# - name: entries-iam
#   action: gcp-types/cloudfunctions-v1:cloudfunctions.projects.locations.functions.setIamPolicy
#   properties:
#     resource: $(ref.entries.name)
#     policy:
#       bindings:
#       - role: roles/cloudfunctions.invoker
#         members:
#         - allUsers

# Create request to insert deployment
request_body = {
    "name": deployment_name,
    "target": {
        "config": {
            "content": restapi_yaml
        },
        "imports": []
    },
    "labels": []
}
operation = deployment_api.deployments().insert(project=project_id, body=request_body).execute()
op_name = operation['name']
wait_on_operation(op_name, deployment_api, project_id)