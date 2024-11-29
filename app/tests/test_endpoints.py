from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_suggestions():
    response = client.post("/suggestions", json={"user_id": 1})
    assert response.status_code == 200
    assert "suggestions" in response.json()