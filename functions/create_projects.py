from googleapiclient import discovery
import base64
import json
import uuid

coded_string = ""
decoded_credential = base64.b64decode(coded_string)
credentials = json.loads(decoded_credential)
service = discovery.build('cloudresourcemanager', 'v1', credentials=credentials)

def prepare_data(event):
    project_body = {
          "projectId": str(uuid.uuid4())[:2] + event['name'],
          "name": event['name'],
    }
    return project_body

def handler(event,context):
    body = prepare_data(event)
    request = service.projects().create(body=body)
    response = request.execute()
    return response