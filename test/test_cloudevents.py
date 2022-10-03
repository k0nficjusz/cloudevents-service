import pytest
from app import app

from cloudevents.conversion import to_binary, to_structured
from cloudevents.http import CloudEvent


@pytest.fixture
def client():
    app.testing = True
    return app.test_client()


def test_structured_request(client):
    # This data defines a binary cloudevent
    attributes = {
        "type": "com.example.sampletype2",
        "source": "https://example.com/event-producer",
    }
    data = {"message": "Test message in cloudevent!"}

    event = CloudEvent(attributes, data)
    headers, body = to_structured(event)

    r = client.post("/", headers=headers, data=body)
    assert r.status_code == 204
    