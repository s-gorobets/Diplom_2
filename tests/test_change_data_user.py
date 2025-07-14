from data.data import Answer
from conftest import *
import allure

@allure.feature("Изменение данных пользователя")
class TestChangeDataUser:
    @allure.title("Изменение данных пользователя с авторизацией")
    def test_change_autoriz(self, create_user_and_delete):
        token = create_user_and_delete["access_token"]
        headers = {'Authorization': token}
        payload = {'name': 'USERUSSIASIASTANA'}
        response = requests.patch(CHANGE_URL, headers=headers, json=payload)
        assert response.status_code == 200 and response.json()['user']['name'] == payload['name']

    @allure.title("Изменение данных пользователя без авторизации")
    def test_chanse_nonautoriz(self):
        payload = {'name': "USERUSSIASIASTANA"}
        response = requests.patch(CHANGE_URL, json=payload)
        assert response.status_code == 401 and response.json()['message'] == Answer.Unauthorized_autoriz