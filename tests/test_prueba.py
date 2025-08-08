import pytest
import requests
import json

def test_login_exitoso():
    url = "https://directus-production-a253.up.railway.app/auth/login"

    payload = json.dumps({
        "email": "elvisac.contact@gmail.com",
        "password": "etg9xm4py6q6722mdd0feskrhqbbtnq7"
    })
    headers = {
    'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    
    assert response.status_code == 200