import requests
import allure
from constants import Constants


class TestNewCourierApi:

    @allure.title('Проверка логина курьера при отсутствующем поле логина')
    def test_new_courier_api(self, create_new_courier_and_del):
         payload = create_new_courier_and_del
         response = requests.post(Constants.URL + Constants.END_COURIER, data=payload)
         r = response.json()
         assert response.status_code == 201
         assert r['ok']

