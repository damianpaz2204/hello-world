from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_greet_query():
    response = client.get("/greet/Damian")
    assert response.status_code == 200
    assert response.json() == {"message": "hello damian"}
