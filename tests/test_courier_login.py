import allure
import requests
import pytest
from methods.courier_methods import CourierMethods
from data import TestMessages, existing_user_payload


class TestLoginCourier:

    @allure.title('Авторизация курьера')
    def test_courier_authorization_success(self):
        courier = CourierMethods()
        response = courier.courier_authorization(existing_user_payload)
        assert (response.status_code == TestMessages.COURIER_AUTHORIZATION_SUCCESS["code"] and response.json()["id"] != TestMessages.COURIER_AUTHORIZATION_SUCCESS["message"])


    @allure.title('Проверка ошибки при отсутствии логина')
    def test_login_missing_login_failure(self):
        payload = {
            "login": "",
            "password": existing_user_payload["password"]
         }
        courier = CourierMethods()
        response = courier.courier_authorization(payload)
        assert (response.status_code == TestMessages.COURIER_NOT_ENOUGH_AUTHORIZATION_DATA["code"] and response.json()["message"] == TestMessages.COURIER_NOT_ENOUGH_AUTHORIZATION_DATA["message"])

    @allure.title('Проверка ошибки при отсутствии пароля')
    def test_login_missing_password_failure(self):
        payload = {
            "login": existing_user_payload["login"],
            "password": ""
        }
        courier = CourierMethods()
        response = courier.courier_authorization(payload)
        assert (response.status_code == TestMessages.COURIER_NOT_ENOUGH_AUTHORIZATION_DATA["code"] and response.json()[
            "message"] == TestMessages.COURIER_NOT_ENOUGH_AUTHORIZATION_DATA["message"])

    @allure.title('Авторизация курьера с невалидным логином')
    def test_courier_not_existing_login_failure(self):
        payload = {
            "login": existing_user_payload["wrong_login"],
            "password": existing_user_payload["password"]
        }
        courier = CourierMethods()
        response = courier.courier_authorization(payload)
        assert (response.status_code == TestMessages.COURIER_ACCOUNT_NOT_FOUND["code"] and response.json()["message"] == TestMessages.COURIER_ACCOUNT_NOT_FOUND["message"])

    @allure.title('Авторизация курьера с невалидным паролем')
    def test_courier_not_existing_login_failure(self):
        payload = {
            "login": existing_user_payload["login"],
            "password": "wrong_pass"
        }
        courier = CourierMethods()
        response = courier.courier_authorization(payload)
        assert (response.status_code == TestMessages.COURIER_ACCOUNT_NOT_FOUND["code"] and response.json()["message"] ==
                TestMessages.COURIER_ACCOUNT_NOT_FOUND["message"])
