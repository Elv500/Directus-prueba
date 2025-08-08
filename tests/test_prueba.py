import pytest
import requests
import json

def test_login_exitoso():
    url = "https://directus-production-a253.up.railway.app/auth/login"

    payload = json.dumps({
    "email": "admin@example.com",
    "password": "d1r3ctu5"
    })
    headers = {
    'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    
    assert response.status_code == 200