import allure
from methods.order_methods import OrderMethods
from data import TestMessages

class TestListOfOrders:

    @allure.title('Получение списка заказов')
    def test_get_orders_list_success(self):
        order_methods = OrderMethods()
        response = order_methods.load_orders()
        response_body = response.json()
        orders = response_body['orders']
        assert (response.status_code == TestMessages.ORDER_LIST_OF_ORDERS_SUCCESS["code"] and all('track' in order for order in orders))