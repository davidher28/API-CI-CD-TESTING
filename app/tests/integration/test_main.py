from fastapi.testclient import TestClient

from app.main import app


def test_hello_world_endpoint():
    # Arrange
    client: TestClient = TestClient(app)
    expected: dict = {"message": "Hello World!"}

    # Act
    response = client.get("/")

    # Assert
    assert response.status_code == 200
    assert response.json() == expected
    assert isinstance(response.json(), dict) == isinstance(expected, dict)
