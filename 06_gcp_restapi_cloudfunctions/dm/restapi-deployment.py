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
    h = httplib2.Http()
    headers = {'Content-Type': 'application/zip',
            'x-goog-content-length-range': '0,104857600'}
    with open('./function.zip', 'rb') as f:
        h.request(upload_url, method='PUT', headers=headers, body=f)
    # Delete zip
    os.remove('./function.zip')
    print(f'Created and uploaded zip file with function code to {upload_url}')
    time.sleep(1)
    return upload_url

def generateDeploymentYaml(project_id, location_name, upload_url, function_name):
    yaml = f'''
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
    return yaml

def deploy(deployment_api, deployment_name, project_id, location_name, yaml):
    # Create request to insert deployment
    request_body = {
        "name": deployment_name,
        "target": {
            "config": {
                "content": yaml
            },
            "imports": []
        },
        "labels": []
    }
    operation = deployment_api.deployments().insert(project=project_id, body=request_body).execute()
    op_name = operation['name']
    wait_on_operation(op_name, deployment_api, project_id)
    print(f'\nFinished deployment operation: {operation}')
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

yaml = f'''resources:
{generateDeploymentYaml(project_id, location_name, upload_url, 'entries')}
{generateDeploymentYaml(project_id, location_name, upload_url, 'entry')}'''

print(f'Launching deployment using specification: \n {yaml}')
deploy(deployment_api, deployment_name, project_id, location_name, yaml)
print(f'baseApiUrl for guestbook.js is https://{location_name}-{project_id}.cloudfunctions.net/')