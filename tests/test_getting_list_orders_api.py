import allure
import requests
from constants import Constants


class TestGettingListOrders:

    @allure.title('Проверка получения списка заказов')
    def test_getting_list_orders_api(self):
        response = requests.get(Constants.URL + Constants.END_ORDERS)
        r = response.json()
        assert "orders" in r
