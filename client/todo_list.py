import requests
import constants
import json
from common import JSON_HEADERS

TODO_LIST_URL = f'{constants.API_BASE_URL}/list'


def create_todo_list(list_name):
    payload = {
        "list_name": list_name
    }
    response = requests.post(TODO_LIST_URL,
                             data=json.dumps(payload),
                             headers=JSON_HEADERS)
    return response.json()


def view_todo_list(list_id):
    response = requests.get(f'{TODO_LIST_URL}/{list_id}',
                            headers=JSON_HEADERS)
    return response.json()


def delete_todo_list(list_id):
    response = requests.delete(f'{TODO_LIST_URL}/{list_id}',
                               headers=JSON_HEADERS)
    return response.status_code == 204


def add_list_item(list_id, item_name):
    payload = {
        "todo_item_name": item_name
    }
    response = requests.post(f"{TODO_LIST_URL}/{list_id}",
                             data=json.dumps(payload),
                             headers=JSON_HEADERS)
    return response.json()


def update_list_item(list_id, list_item_id, item_name):
    payload = {
        "todo_item_name": item_name
    }
    response = requests.put(f"{TODO_LIST_URL}/{list_id}/{list_item_id}",
                            data=json.dumps(payload),
                            headers=JSON_HEADERS)
    return response.json()


def delete_list_item(list_id, list_item_id):
    response = requests.delete(f"{TODO_LIST_URL}/{list_id}/{list_item_id}",
                               headers=JSON_HEADERS)
    return response.status_code == 204


