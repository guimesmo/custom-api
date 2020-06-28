import requests
import constants
import json
import os
from common import JSON_HEADERS

USER_REGISTER_URL = f'{constants.API_BASE_URL}/register'
USER_LOGIN_URL = f'{constants.API_BASE_URL}/login'


def register_user(email, password, first_name, last_name):
    payload = {
        "email": email,
        "password": password,
        "first_name": first_name,
        "last_name": last_name
    }
    response = requests.post(USER_REGISTER_URL,
                             data=json.dumps(payload),
                             headers=JSON_HEADERS)
    return response.status_code == 204


def login_user(email, password):
    payload = {
        "username": email,
        "password": password
    }
    print(payload)
    response = requests.post(USER_LOGIN_URL,
                             data=json.dumps(payload),
                             headers=JSON_HEADERS)
    if response.status_code != 200:
        print("Login failed")
        print(response.content)
        return

    user_token = response.json().get('token')

    os.environ['app_token'] = user_token
    return response.json()
