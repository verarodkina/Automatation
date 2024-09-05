import pytest
import requests
from Homework.Test.constants import x_client_url

@pytest.fixture()
def get_token(username='raphael', password='cool-but-crude'):
    log_pass = {'username':username, 'password':password}
    resp_token = requests.post(x_client_url + '/auth/login', json = log_pass)
    token = resp_token.json()['userToken']
    return token