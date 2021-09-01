from fastapi.testclient import TestClient
from pytest import mark

from main import app

client = TestClient(app)


def test_hello_endpoint():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


@mark.parametrize('specific_message', ('John Doe', 'Foo', 'Jane Dow'))
def test_hello_with_specific_message_endpoint(specific_message):
    response = client.get(f"/hello/{specific_message}")
    assert response.status_code == 200
    assert response.json() == {"message": f"Hello, {specific_message}"}
