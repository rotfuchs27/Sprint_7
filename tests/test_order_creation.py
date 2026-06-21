import allure
import pytest
from methods.order_methods import OrderMethods

class TestCreateOrder:

    @pytest.mark.parametrize("color", [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    @allure.title("Параметризованный тест для создания заказа с разными цветами самоката")
    def test_create_order_successful(self, color):
        order_data = {
            "firstName": "Иммануил",
            "lastName": "Кант",
            "address": "Николоямская улица, 8с1",
            "metroStation": 7,
            "phone": "+7 9653212121",
            "rentTime": 3,
            "deliveryDate": "2026-06-06",
            "comment": "Позвонить за час до доставки",
            "color": color
        }
        order_methods = OrderMethods()
        response = order_methods.create_order(order_data)
        assert ("track" in response.json() and response.status_code == 201)