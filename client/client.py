"""
Main file of client application

Available commands:
    - register-user <email> <password> <first_name> <last_name>
    - login-user <email> <password>
    - create-list <list_name>
    - view-list <list_id>
    - delete-list <list_id>
    - add-list-item <list_id> <item_name>
    - update-list-item <list_id> <item_id>
    - delete-list-item <list_id> <item_id>
"""
import pprint

from common import parse_args, ValidationError, TokenError
from todo_list import create_todo_list, view_todo_list, delete_todo_list, add_list_item, update_list_item, \
    delete_list_item
from user import login_user, register_user


def register_user_action():
    try:
        args = parse_args(4, 1)
        pprint.pprint(register_user(*args))
    except ValidationError:
        print("Please inform email, password, first and last name")


def login_user_action():
    try:
        args = parse_args(2, 1)
        pprint.pprint(login_user(*args))
    except ValidationError:
        print("Please inform the email and password")


def create_list_action():
    try:
        args = parse_args(1, 1)
        pprint.pprint(create_todo_list(*args))
    except ValidationError:
        print("The name is required for todo list")


def view_list_action():
    try:
        args = parse_args(1, 1)
        pprint.pprint(view_todo_list(*args))
    except ValidationError:
        print("The id is required for todo list view")


def delete_list_action():
    try:
        args = parse_args(1, 1)
        pprint.pprint(delete_todo_list(*args))
    except ValidationError:
        print("The id is required for todo list delete")


def add_list_item_action():
    try:
        args = parse_args(2, 1)
        pprint.pprint(add_list_item(*args))
    except ValidationError:
        print("The list id is required")


def update_list_item_action():
    try:
        args = parse_args(3, 1)
        pprint.pprint(update_list_item(*args))
    except ValidationError:
        print("The list id and item id are required for todo item update")


def delete_list_item_action():
    try:
        args = parse_args(2, 1)
        pprint.pprint(delete_list_item(*args))
    except ValidationError:
        print("The list id and item id are required for todo item delete")


def main():
    available_actions = {
        'register-user': register_user_action,
        'login': login_user_action,
        'create-list': create_list_action,
        'view-list': view_list_action,
        'delete-list': delete_list_action,
        'add-list-item': add_list_item_action,
        'update-list-item': update_list_item_action,
        'delete-list-item': delete_list_item_action,
    }
    try:
        action = parse_args(1)[0]
    except ValidationError:
        print("Missing action:")
        for ac in available_actions.keys():
            print(ac)
        return

    executable_action = available_actions.get(action)
    if not executable_action:
        print("Invalid argument.")
        return

    # call action
    try:
        executable_action()
    except TokenError:
        print("You must login before this action")


if __name__ == "__main__":
    main()
