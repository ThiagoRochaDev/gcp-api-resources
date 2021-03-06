from googleapiclient import discovery
import base64
import json

coded_string = ""
decoded_credential = base64.b64decode(coded_string)
credentials = json.loads(decoded_credential)
service = discovery.build('cloudresourcemanager', 'v1', credentials=credentials)

def handler(event, context):
    project_id = event.get('pathParameters')
    request = service.projects().delete(projectId=project_id)
    request.execute()