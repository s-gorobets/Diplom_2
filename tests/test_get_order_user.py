from conftest import *
import requests
from data.data import Answer
import allure
@allure.feature("Получение заказов пользователя")
class TestGetOrder:
    @allure.title("Получение заказов авторизованного пользователя")
    def test_get_order_autoriz_user(self, create_user_and_delete):
        token = create_user_and_delete["access_token"]
        headers = {'Authorization': token}
        response = requests.get(ORDER_URL, headers=headers)
        print(response.json())
        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title("Получение заказов неавторизованного пользователя")
    def test_get_order_nonautoriz_user(self):
        response = requests.get(ORDER_URL)
        print(response.json())
        assert response.status_code == 401 and response.json()['message'] == Answer.Unauthorized_Get_Order