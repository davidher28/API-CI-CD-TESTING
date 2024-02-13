from app.services.hello_world import hello_world


def test_hello_world():
    # Arrange
    expected: str = "Hello World!"

    # Act
    response: str = hello_world()

    # Assert
    assert response == expected
    assert isinstance(response, str) == isinstance(expected, str)
