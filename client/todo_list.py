import requests
import constants
import json
from common import build_url
from common import JSON_HEADERS

TODO_LIST_URL = build_url(constants.API_BASE_URL, 'list/')


def create_todo_list(list_name):
    payload = {
        "list_name": list_name
    }
    response = requests.post(TODO_LIST_URL,
                             data=json.dumps(payload),
                             headers=JSON_HEADERS)
    return response.json()


def view_todo_list(list_id):
    response = requests.get(f'{TODO_LIST_URL}{list_id}',
                            headers=JSON_HEADERS)
    return response.json()

