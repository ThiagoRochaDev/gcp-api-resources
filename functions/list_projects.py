from googleapiclient import discovery
import base64
import json

coded_string = ""
decoded_credential = base64.b64decode(coded_string)
credentials = json.loads(decoded_credential)

service = discovery.build('cloudresourcemanager', 'v1', credentials=credentials)

while True:
    request = service.projects().list()
    response = request.execute()

    for project in response.get('projects', []):
        # TODO: Change code below to process each `project` resource:
        pprint(project)

    request = service.projects().list_next(previous_request=request, previous_response=response)