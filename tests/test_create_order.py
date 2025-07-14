from conftest import *
import requests
from data.data import Answer
import allure

@allure.feature("Создание заказа")
class TestCreateOrder:
    @allure.title("Создание заказа с авторизацией и ингредиентами")
    def test_create_order_autoriz(self, create_user_and_delete):
        token = create_user_and_delete["access_token"]
        headers = {'Authorization': token}
        payload = {"ingredients": ["61c0c5a71d1f82001bdaaa6d",
                                   "61c0c5a71d1f82001bdaaa70"]
                   }
        response = requests.post(ORDER_URL, headers=headers, json=payload)
        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title("Создание заказа без авторизации и с ингредиентами")
    def test_create_order_non_autoriz(self):
        payload = {"ingredients": ["61c0c5a71d1f82001bdaaa6d",
                                   "61c0c5a71d1f82001bdaaa70"]
                   }
        response = requests.post(ORDER_URL, json=payload)
        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title("Создание заказа без ингредиентов")
    def test_create_order_noningridient(self):
        payload = {"ingredients": []}
        response = requests.post(ORDER_URL, json=payload)
        assert response.status_code == 400 and response.json()['message'] == Answer.BadRequest

    @allure.title("Создание заказа с неверным хешем ингредиентов")
    def test_create_order_incorrect_hash(self):
        payload = {"ingredients": ["61c0c5a71d1f82001bsaaa6d",
                                   "61c0c5a71d1asd001bdaaa70"]
                   }
        response = requests.post(ORDER_URL, json=payload)
        assert response.status_code == 500
