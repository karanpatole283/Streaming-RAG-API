from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_query_endpoint():
    response = client.post("/query", json={"query": "python", "top_k": 2})
    assert response.status_code == 200
    assert "Python is a popular programming language." in response.text
