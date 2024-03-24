import requests
import allure
from constants import Constants
from data import Data
from helper import Helper


class TestNewCourierWithoutAnyData:

    @allure.title('Проверка создания курьера при отсутствующем поле логина')
    def test_courier_without_login(self):

        payload = {'password': Helper.generate_random_string(), 'firstname': Helper.generate_random_string()}
        response = requests.post(Constants.URL + Constants.END_COURIER, data=payload)
        r = response.json()
        assert response.status_code == 400
        assert r['message'] == Data.error_crate_courier_without_data

    @allure.title('Проверка создания курьера при отсутствующем поле пароля')
    def test_courier_without_password(self):
        payload = {'login': Helper.generate_random_string(), 'firstname': Helper.generate_random_string()}
        response = requests.post(Constants.URL + Constants.END_COURIER, data=payload)
        r = response.json()
        assert response.status_code == 400
        assert r['message'] == Data.error_crate_courier_without_data

    @allure.title('Проверка создания курьера при отсутствующем поле имени')
    def test_courier_without_firstname(self):
        payload = {'login': Helper.generate_random_string(), 'password': Helper.generate_random_string()}
        response = requests.post(Constants.URL + Constants.END_COURIER, data=payload)
        r = response.json()
        assert response.status_code == 400
        assert r['message'] == Data.error_crate_courier_without_data
