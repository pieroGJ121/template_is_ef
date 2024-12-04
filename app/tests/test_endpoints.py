from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_suggestions_genre_success():
    response = client.post("/suggestions/genre", json={"genres": ["Crime"]})
    assert response.status_code == 200
    assert "suggestions" in response.json()


def test_get_suggestions_genre_422():
    response = client.post("/suggestions/genre", json={"s12": [1234]})
    assert response.status_code == 422


# def test_get_suggestions_genre_500():
#     response = client.post("/suggestions/genre", json={"s12": ["asdasfa"]})
#     assert response.status_code == 500
