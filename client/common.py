import os
import sys

JSON_HEADERS = {'content-type': 'application/json'}


class ValidationError(Exception):
    pass


class TokenError(Exception):
    pass


def get_headers_auth():
    """Get application/json headers with Authorization token"""
    auth_token = os.getenv("app_token")
    if not auth_token:
        raise TokenError("Missing token")

    return {'content-type': 'application/json',
            'Authorization': f'Token {auth_token}'}


def get_args():
    for index, cmd in enumerate(sys.argv):
        if cmd.endswith('.py'):
            return sys.argv[index + 1:]
    return sys.argv


def parse_args(number_of_args, start_from=0):
    args = get_args()
    if len(args) < number_of_args:
        raise ValidationError("Missing arguments")
    return args[start_from:]
