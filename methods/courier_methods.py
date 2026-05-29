import allure
import requests
from data import CREATE_COURIER, COURIER_LOGIN


class CourierMethods:

    @staticmethod
    @allure.step('Регистрация курьера')
    def courier_registration(courier_data):
        response = requests.post(url=CREATE_COURIER, json=courier_data)
        return response


    @staticmethod
    @allure.step('Авторизация курьера')
    def courier_authorization(courier_data):
        response = requests.post(url=COURIER_LOGIN, json=courier_data)
        return response
