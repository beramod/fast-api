import json
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200    
    assert response.json() == {"message": "octo auth"}
    
def test_login_valid_user():
    url = '/api/v1/authority/login'
    param = {
        'userId': 'admintest',
        'userPass': '123',
    }
    response = client.post(url, data=json.dumps(param))

    assert response.status_code == 200
    assert response.userId == 'userId'