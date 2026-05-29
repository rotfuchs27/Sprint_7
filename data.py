
BASE_URL = 'https://qa-scooter.education-services.ru'
CREATE_COURIER = BASE_URL + '/api/v1/courier'
COURIER_LOGIN = BASE_URL + '/api/v1/courier/login'
ORDER = BASE_URL + '/api/v1/orders'


existing_user_payload = {
            "login": "user",
            "password": "password",
            "first_name": "name"
        }

class TestMessages:

    COURIER_CREATE_SUCCESS = {"code": 201, "message": True}
    COURIER_LOGIN_ALREADY_IN_USE = {"code": 409, "message": "Этот логин уже используется. Попробуйте другой."}
    COURIER_NOT_ENOUGH_DATA = {"code": 400, "message": "Недостаточно данных для создания учетной записи"}
    COURIER_AUTHORIZATION_SUCCESS = {"code": 200, "message": None}
    COURIER_NOT_ENOUGH_AUTHORIZATION_DATA = {"code": 400, "message": "Недостаточно данных для входа"}
    COURIER_ACCOUNT_NOT_FOUND = {"code": 404, "message": "Учетная запись не найдена"}

    ORDER_CREATION_SUCCESS = {"code": 201, "message": "track"}
    ORDER_LIST_OF_ORDERS_SUCCESS = {"code": 200, "message": "orders"}