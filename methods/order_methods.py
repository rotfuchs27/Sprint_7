import allure
import requests
from data import ORDER


class OrderMethods:

    @staticmethod
    @allure.step('Создать заказ')
    def create_order(order_data):
        response = requests.post(url=ORDER, json=order_data)
        return response

    @staticmethod
    @allure.step('Загрузить список заказов')
    def load_orders():
        response = requests.get(url=ORDER)
        return response