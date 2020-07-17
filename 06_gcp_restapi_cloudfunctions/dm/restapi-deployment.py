import google.auth
from googleapiclient import discovery
from google.cloud import storage
import time
import os
import sys
import zipfile
import httplib2

def wait_on_operation(op_name, deployment_api, project_id):
    while True:
        time.sleep(1)
        print('.', end="", flush=True)
        op_status = deployment_api.operations().get(
            project=project_id,
            operation=op_name).execute()['status']
        if op_status == 'DONE':
            break
    return True

def uploadCloudFunction(credentials):
    # Create zipfile for deploying function
    print(f'Creating zip file with Cloud Function code...')
    with zipfile.ZipFile('./function.zip', 'w') as z:
        z.write('../main.py', 'main.py')
        z.write('../requirements.txt', 'requirements.txt')
        for dir_path, subdir_paths, f_names in os.walk('../gbmodel'):
            for f in f_names:
                file_path = dir_path + '/' + f
                arc_path = file_path.replace('../', '')
                z.write(file_path, arcname=arc_path)
    # Instantiate Cloud Function API
    cf_api = discovery.build('cloudfunctions', 'v1', credentials=credentials)
    parent = f'projects/{project_id}/locations/{location_name}'
    # Generate upload URL from Cloud Function API
    upload_url = cf_api.projects().locations().functions().generateUploadUrl(parent=parent).execute()['uploadUrl']
    # Upload function
    print(f'Uploading function.zip to temporary bucket')
    h = httplib2.Http()
    headers = {'Content-Type': 'application/zip',
            'x-goog-content-length-range': '0,104857600'}
    with open('./function.zip', 'rb') as f:
        h.request(upload_url, method='PUT', headers=headers, body=f)
    # Delete zip
    os.remove('./function.zip')
    return upload_url

def deployFunction(deployment_api, deployment_name, project_id, location_name, upload_url, function_name):
    restapi_yaml = f'''
    resources:
    - type: gcp-types/cloudfunctions-v1:projects.locations.functions
      name: {function_name}
      properties:
        function: {function_name}
        parent: projects/{project_id}/locations/{location_name}
        sourceUploadUrl: {upload_url}
        entryPoint: {function_name}
        runtime: python37
        httpsTrigger: {{}}
        serviceAccountEmail: guestbook@{project_id}.iam.gserviceaccount.com
    - name: {function_name}-iam
      action: gcp-types/cloudfunctions-v1:cloudfunctions.projects.locations.functions.setIamPolicy
      properties:
        resource: $(ref.{function_name}.name)
        policy:
          bindings:
          - role: roles/cloudfunctions.invoker
            members:
            - allUsers
    '''

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
    print(f"Launching deployment of /{function_name} endpoint")
    operation = deployment_api.deployments().insert(project=project_id, body=request_body).execute()
    print(operation)
    print(operation['name'])
    op_name = operation['name']
    wait_on_operation(op_name, deployment_api, project_id)
    print(f'\nFinished operation.  /{function_name} endpoint available at: https://{location_name}-{project_id}.cloudfunctions.net/{function_name}')
    return True

# Instantiate Deployment Manager API
credentials, project_id = google.auth.default()

location_name = 'us-central1'
if len(sys.argv) != 2:
    print("Usage: python restapi-deployment.py <NameOfDeployment>")
    exit()
else:
    deployment_name = sys.argv[1]
service_account = f"guestbook@{project_id}.iam.gserviceaccount.com"

# Upload Cloud Function code
upload_url = uploadCloudFunction(credentials)

deployment_api = discovery.build('deploymentmanager', 'v2', credentials=credentials)

deployFunction(deployment_api, deployment_name, project_id, location_name, upload_url, 'entries')