import requests
import allure
from constants import Constants


class TestLoginCourier:

    @allure.title('Проверка логина курьера')
    def test_login_courier(self, create_new_courier_and_del):
        payload = create_new_courier_and_del
        payload_login = payload
        del payload_login['firstName']
        requests.post(Constants.URL + Constants.END_COURIER, data=payload)
        response = requests.post(Constants.URL+Constants.END_LOGIN, data=payload_login)

        assert response.status_code == 200
        assert 'id' in response.json()
