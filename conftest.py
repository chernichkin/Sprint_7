import requests
import random
import string
import pytest
from constants import Constants
from helper import Helper

@pytest.fixture
def create_new_courier_and_del():
    password = Helper.generate_random_string()
    login = Helper.generate_random_string()
    user = {'login': login, "password": password, "firstName": "saske"}
    user_login = {'login': login, "password": password}
    yield user
    response = requests.post(Constants.URL + '/api/v1/courier/login', data=user_login)
    id_courier = response.json()['id']
    requests.delete(Constants.URL + f'/api/v1/courier/{id_courier}')

