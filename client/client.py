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
import sys
import pprint

from todo_list import create_todo_list, view_todo_list


def main():
    action = sys.argv[1]
    print(action)

    if action == 'create-list':
        try:
            pprint.pprint(create_todo_list(sys.argv[2]))
        except IndexError:
            print("The name is required for todo list")
            exit(0)

    if action == 'view-list':
        try:
            pprint.pprint(view_todo_list(sys.argv[2]))
        except IndexError:
            print("The id is required for todo list view")
            exit(0)
    else:
        print("Invalid argument")
        exit(0)


if __name__ == "__main__":
    main()
