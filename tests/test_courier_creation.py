import allure
import requests
from data import TestMessages, CREATE_COURIER, existing_user_payload
from methods.courier_methods import CourierMethods
from helper import generate_random_string



class TestCreateCourier:

    @allure.title('Создание курьера')
    def test_create_courier_success(self):
        payload = {
            "login": generate_random_string(),
            "password": generate_random_string(),
            "first_name": generate_random_string()
        }
        courier = CourierMethods()
        response = courier.courier_registration(payload)
        assert (response.status_code == TestMessages.COURIER_CREATE_SUCCESS["code"] and response.json()["ok"] == TestMessages.COURIER_CREATE_SUCCESS["message"])

        #удаляем пользователя после создания
        login_response = courier.courier_authorization(payload)
        if login_response.status_code == 200:
            courier_id = login_response.json()["id"]
            requests.delete(f'{CREATE_COURIER}/{courier_id}')


    @allure.title('Нельзя создать двух одинаковых курьеров')
    def test_create_two_identical_couriers_failure(self):
        courier = CourierMethods()
        response = courier.courier_registration(existing_user_payload)
        assert (response.status_code == TestMessages.COURIER_LOGIN_ALREADY_IN_USE["code"] and response.json()["message"] == TestMessages.COURIER_LOGIN_ALREADY_IN_USE["message"])


    @allure.title('Регистрация курьера без параметра login')
    def test_create_courier_without_login_failure(self):
        payload = {
            "login": "",
            "password": generate_random_string(),
            "first_name": generate_random_string()
        }
        courier = CourierMethods()
        response = courier.courier_registration(payload)
        assert (response.status_code == TestMessages.COURIER_NOT_ENOUGH_DATA["code"] and response.json()["message"] == TestMessages.COURIER_NOT_ENOUGH_DATA["message"])


    @allure.title('Регистрация курьера без параметра password')
    def test_create_courier_without_password_failure(self):
        payload = {
            "login": generate_random_string(),
            "password": "",
            "first_name": generate_random_string()
        }
        courier = CourierMethods()
        response = courier.courier_registration(payload)
        assert (response.status_code == TestMessages.COURIER_NOT_ENOUGH_DATA["code"] and response.json()["message"] == TestMessages.COURIER_NOT_ENOUGH_DATA["message"])


    @allure.title('Регистрация курьера без параметра firstName')
    def test_create_courier_without_firstname_success(self):
        payload = {
            "login": generate_random_string(),
            "password": generate_random_string(),
            "first_name": ""
        }
        courier = CourierMethods()
        response = courier.courier_registration(payload)
        assert (response.status_code == TestMessages.COURIER_CREATE_SUCCESS["code"] and response.json()["ok"] == TestMessages.COURIER_CREATE_SUCCESS["message"])