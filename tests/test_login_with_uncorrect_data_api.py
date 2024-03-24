import requests
import allure
from constants import Constants
from data import Data


class TestLoginWithUncorrectData:
    @allure.title('Проверка логина курьера при некорректном поле логина')
    def test_login_with_uncorrect_login(self, create_new_courier_and_del):
        payload = create_new_courier_and_del
        payload_login = payload.copy()
        del payload_login['firstName']
        payload_login['login'] = Constants.TEST_LOGIN
        requests.post(Constants.URL + '/api/v1/courier', data=payload)
        response = requests.post(Constants.URL+'/api/v1/courier/login', data=payload_login)
        r = response.json()

        assert response.status_code == 404
        assert r['message'] == Data.error_uncorrect_login

    @allure.title('Проверка логина курьера при некорректном поле пароля')
    def test_login_with_uncorrect_password(self, create_new_courier_and_del):
        payload = create_new_courier_and_del
        payload_login = payload.copy()
        del payload_login['firstName']
        payload_login['password'] = Constants.TEST_PASSWORD
        requests.post(Constants.URL + Constants.END_COURIER, data=payload)
        response = requests.post(Constants.URL + Constants.END_LOGIN, data=payload_login)
        r = response.json()

        assert response.status_code == 404
        assert r['message'] == Data.error_uncorrect_login
