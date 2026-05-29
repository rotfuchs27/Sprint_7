import allure
import requests
from data import TestMessages
from methods.courier_methods import CourierMethods



class TestCreateCourier:

    @allure.title('Создание курьера')
    def test_create_courier_success(self, generate_random_string):
        payload = {
            "login": generate_random_string,
            "password": generate_random_string,
            "first_name": generate_random_string
        }
        courier = CourierMethods()
        response = courier.courier_registration(payload)
        assert (response.status_code == TestMessages.COURIER_CREATE_SUCCESS["code"] and response.json()["ok"] == TestMessages.COURIER_CREATE_SUCCESS["message"])



    @allure.title('Нельзя создать двух одинаковых курьеров')
    def test_create_two_identical_couriers_failure(self, existing_user_payload):
        courier = CourierMethods()
        response = courier.courier_registration(existing_user_payload)
        assert (response.status_code == TestMessages.COURIER_LOGIN_ALREADY_IN_USE["code"] and response.json()["message"] == TestMessages.COURIER_LOGIN_ALREADY_IN_USE["message"])


    @allure.title('Регистрация курьера без параметра login')
    def test_create_courier_without_login_failure(self, generate_random_string):
        payload = {
            "login": "",
            "password": generate_random_string,
            "first_name": generate_random_string
        }
        courier = CourierMethods()
        response = courier.courier_registration(payload)
        assert (response.status_code == TestMessages.COURIER_NOT_ENOUGH_DATA["code"] and response.json()["message"] == TestMessages.COURIER_NOT_ENOUGH_DATA["message"])


    @allure.title('Регистрация курьера без параметра password')
    def test_create_courier_without_password_failure(self, generate_random_string):
        payload = {
            "login": generate_random_string,
            "password": "",
            "first_name": generate_random_string
        }
        courier = CourierMethods()
        response = courier.courier_registration(payload)
        assert (response.status_code == TestMessages.COURIER_NOT_ENOUGH_DATA["code"] and response.json()["message"] == TestMessages.COURIER_NOT_ENOUGH_DATA["message"])


    @allure.title('Регистрация курьера без параметра firstName')
    def test_create_courier_without_firstname_success(self, generate_random_string):
        payload = {
            "login": generate_random_string,
            "password": generate_random_string,
            "first_name": ""
        }
        courier = CourierMethods()
        response = courier.courier_registration(payload)
        assert (response.status_code == TestMessages.COURIER_CREATE_SUCCESS["code"] and response.json()["ok"] == TestMessages.COURIER_CREATE_SUCCESS["message"])