import json

import pytest
import requests

from constants import Constants


class TestCreateNewOrder:
    @pytest.mark.parametrize('color', [["GREY"], ["BLACK"], ["BLACK", "GREY"], []])
    def test_create_new_order_api(self, color):
        payload = json.dumps({
            "firstName": "Anton",
            "lastName": "Tupov",
            "address": "Извилистая, 13",
            "metroStation": 4,
            "phone": "+7 999 99 99 99",
            "rentTime": 5,
            "deliveryDate": "2020-06-06",
            "comment": "Я ничего не понимаю уже, дайте самокат",
            "color": color
        })

        response = requests.post(Constants.URL + '/api/v1/orders', data=payload)
        r = response.json()
        assert 'track' in r
