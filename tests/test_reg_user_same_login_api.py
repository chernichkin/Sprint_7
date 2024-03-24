import requests
import allure
from constants import Constants
from data import Data
from helper import Helper

class TestUserSameLogin:
    
    @allure.title('Проверка создания курьера с логином, который уже существует')
    def test_user_same_login(self, create_new_courier_and_del):
        payload = create_new_courier_and_del
        login = payload['login']
        payload_same_login = {'login': login, "password": Helper.generate_random_string(), "firstName": Helper.generate_random_string()}
        requests.post(Constants.URL + Constants.END_COURIER, data=payload)
        response = requests.post(Constants.URL + Constants.END_COURIER, data=payload_same_login)
        r = response.json()
        assert response.status_code == 409
        assert r['message'] == Data.error_same_courier
