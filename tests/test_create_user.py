import requests
from data.helpers import *
from data.urls import *
from data.data import Answer, DataUser
import allure

@allure.feature("Регистрация пользователя")
class TestCreateUser:
    @allure.title("Создание уникального пользователя")
    def test_user_create(self):
        payload = {"email": fake_email(),
                   "password": fake_pass(),
                   "name": fake_name()
                }
        response = requests.post(CREATE_USER_URL, payload)
        assert response.status_code == 200

    @allure.title("Создание пользователя, который уже зарегистрирован")
    def test_user_existing(self):
        payload = DataUser.User_existing
        response = requests.post(CREATE_USER_URL, payload)
        assert response.status_code == 403 and response.json()['message'] == Answer.Forbidden

    @allure.title("Создание пользователя без обязательного поля")
    def test_missing_field(self):
        payload = {"email": fake_email(),
                   "password": fake_pass()
                   }
        response = requests.post(CREATE_USER_URL, payload)
        assert response.status_code == 403 and response.json()['message'] == Answer.Forbidden_field