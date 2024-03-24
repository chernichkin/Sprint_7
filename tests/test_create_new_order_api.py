import json

import pytest
import requests
import allure
from data import Data

from constants import Constants


class TestCreateNewOrder:

    @allure.title('Проверка создания нового заказа')
    @pytest.mark.parametrize('color', [["GREY"], ["BLACK"], ["BLACK", "GREY"], []])
    def test_create_new_order_api(self, color):
        def_user = Data.default_user.copy()
        def_user["color"] = color
        payload = json.dumps(def_user)
        response = requests.post(Constants.URL + Constants.END_ORDERS, data=payload)
        r = response.json()
        assert 'track' in r
