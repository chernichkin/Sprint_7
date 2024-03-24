import requests
import allure
from constants import Constants
from data import Data


class TestLoginWithoutAnyData:

    @allure.title('Проверка логина курьера при отсутствующем поле логина')
    def test_login_without_login(self, create_new_courier_and_del):
        payload = create_new_courier_and_del
        payload_login = payload.copy()
        del payload_login['firstName'], payload_login['login']
        requests.post(Constants.URL + Constants.END_COURIER, data=payload)
        response = requests.post(Constants.URL + Constants.END_LOGIN, data=payload_login)
        r = response.json()
        assert response.status_code == 400
        assert r['message'] == Data.error_login_without_login

    @allure.title('Проверка логина курьера при отсутствующем поле пароля')
    def test_login_without_password(self, create_new_courier_and_del):
        payload = create_new_courier_and_del
        payload_login = payload.copy()
        del payload_login['firstName'], payload_login['login']
        requests.post(Constants.URL + Constants.END_COURIER, data=payload)
        response = requests.post(Constants.URL + Constants.END_LOGIN, data=payload_login)
        r = response.json()
        assert response.status_code == 400
        assert r['message'] == Data.error_login_without_login

