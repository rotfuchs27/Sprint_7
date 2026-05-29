import allure
import requests
from data import TestMessages, ORDER

class TestListOfOrders:

    @allure.title('Получение списка заказов')
    def test_get_orders_list_success(self):
        response = requests.get(url=ORDER)
        response_body = response.json()
        orders = response_body['orders']
        assert (response.status_code == TestMessages.ORDER_LIST_OF_ORDERS_SUCCESS["code"] and all('track' in order for order in orders))