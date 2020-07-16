import google.auth
from googleapiclient import discovery
from googleapiclient.errors import HttpError
from google.cloud import storage
import os
import time

def wait_on_operation(opname, deployment_api, project_id):
    while True: 
        time.sleep(1)
        print('.',end="",flush=True)
        op_status = deployment_api.operations().get(
            project=project_id,
            operation=op_name).execute()['status']
        if op_status == 'DONE':
            break;
    return True

deployment_name = f"{os.environ['GOOGLE_CLOUD_PROJECT']}-frontend"
credentials, project_id = google.auth.default()
deployment_api = discovery.build('deploymentmanager', 'v2', credentials=credentials)

frontend_yaml = f''' resources:
  - type: gcp-types/storage-v1:buckets
    name: {deployment_name}
    properties:
      region: us-west1
      storageClass: STANDARD
      acl:
        - role: READER
          entity: allUsers
      defaultObjectAcl:
        - entity: allUsers
          role: READER
'''

# Create request to insert deployment
request_body = {
    "name": deployment_name,
    "target": {
        "config": {
            "content": frontend_yaml
        },
        "imports": []
    },
    "labels": []
}
operation = deployment_api.deployments().insert(project=project_id, body=request_body).execute()
op_name = operation['name']
wait_on_operation(op_name, deployment_api, project_id)

storage_client = storage.Client()
bucket = storage_client.bucket(deployment_name)
for object_file in ['index.html', 'static/guestbook.js', 'static/style.css']:
    blob = bucket.blob(object_file)
    blob.upload_from_filename(f'../frontend-src/{object_file}')
