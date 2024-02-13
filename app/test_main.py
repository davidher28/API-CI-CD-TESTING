from fastapi.testclient import TestClient

from .main import app, hello_world


def test_hello_world():
    # Arrange
    expected = "Hello Barcelona!"

    # Act
    response = hello_world()

    # Assert
    assert response == expected


def test_hello_world_endpoint():
    # Arrange
    client = TestClient(app)
    expected = {"message": "Hello Barcelona!"}

    # Act
    response = client.get("/")

    # Assert
    assert response.status_code == 200
    assert response.json() == expected
