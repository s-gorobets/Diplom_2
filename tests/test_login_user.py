from conftest import *
import requests
from data.data import Answer, DataUser
import allure

@allure.feature("Логин пользователя")
class TestLoginUser:
    def test_login_existing_user(self, create_user_and_delete):
        payload = {
            "email": create_user_and_delete["email"],
            "password": create_user_and_delete["password"]
        }
        response = requests.post(LOGIN_USER_URL, payload)
        assert response.status_code == 200 and "accessToken" in response.json() and "refreshToken" in response.json()

    @allure.title("Логин с неверным логином и паролем")
    def test_nonexistent_login_user(self):
        response = requests.post(LOGIN_USER_URL, json=DataUser.Invalid_user)
        assert response.status_code == 401 and response.json()['message'] == Answer.Unauthorized

