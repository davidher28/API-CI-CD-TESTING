from fastapi.testclient import TestClient
from httpx import Response

from app.main import app


def test_hello_world_endpoint():
    # Arrange
    client: TestClient = TestClient(app)
    expected: dict = {"message": "Hello World!"}

    # Act
    response: Response = client.get("/")

    # Assert
    assert response.status_code == 200
    assert response.json() == expected
    assert isinstance(response.json(), dict) == isinstance(expected, dict)
