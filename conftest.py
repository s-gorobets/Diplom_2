import pytest
import requests
import uuid
from data.urls import *

@pytest.fixture
def create_user_and_delete():
    email = f"test_{uuid.uuid4().hex[:8]}@example.com"
    password = "test123"
    name = "Test User"

    payload = {"email": email, "password": password, "name": name}
    response = requests.post(REGISTER_URL, json=payload)
    assert response.status_code == 200

    tokens = response.json()
    access_token = tokens["accessToken"]
    refresh_token = tokens["refreshToken"]

    yield {
        "email": email,
        "password": password,
        "name": name,
        "access_token": access_token,
        "refresh_token": refresh_token,
    }

    headers = {"Authorization": tokens["accessToken"]}
    requests.delete(DELETE_USER_URL, headers=headers)

