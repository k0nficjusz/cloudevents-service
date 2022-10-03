from cloudevents.conversion import to_structured
from cloudevents.http import CloudEvent
import requests

# Create a CloudEvent
# - The CloudEvent "id" is generated if omitted. "specversion" defaults to "1.0".
attributes = {
    "specversion": "1.0",
    "type": "event_type",
    "source": "https://jenkins/",
    "subject": "some_subject",
    "id": "2",
    "time": "2022-10-01T00:54:56+0000",
    "dataschema": "arch_schema",
}
data = {
    "archive_url": "google.com/storage/example_file.txt",
    "data_path": "/run/logs",
    "env_file": "decorator_file",
    "git_repository": "repo_of",
    "git_revision": "b25e3077d9a30f7f204cc37f717466",
    "git_tag": "RELEASE_1.1.1",
    "is_release_build": "false"
}
event = CloudEvent(attributes, data)

# Creates the HTTP request representation of the CloudEvent in structured content mode
headers, body = to_structured(event)

# POST
requests.post("http://127.0.0.1:3000", data=body, headers=headers)
