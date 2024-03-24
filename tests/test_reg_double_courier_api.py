import requests
import allure
from constants import Constants
from data import Data


class TestDoubleCourierApi:

    @allure.title('Проверка создания дубля курьера')
    def test_double_courier_api(self, create_new_courier_and_del):
        payload = create_new_courier_and_del
        requests.post(Constants.URL + Constants.END_COURIER, data=payload)
        response_double = requests.post(Constants.URL + Constants.END_COURIER, data=payload)
        r_double = response_double.json()
        assert response_double.status_code == 409
        assert r_double['message'] == Data.error_same_courier
