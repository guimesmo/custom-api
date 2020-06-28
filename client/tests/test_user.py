import unittest
from unittest import mock

from user import login_user, register_user

from . import mocks


class TestTodoListCreate(unittest.TestCase):
    @mock.patch("requests.post", return_value=mocks.MockNoContentResponse)
    def test_register_user(self, mock_res):
        response = register_user("sample@email.com",
                                 "samplepassword",
                                 "Some name",
                                 "Some last name")
        self.assertEqual(response, "User registered.")

    @mock.patch("requests.post", return_value=mocks.MockValidationErrorResponse)
    def test_register_user_invalid_response(self, mock_res):
        response = register_user("sample@email.com",
                                 "samplepassword",
                                 "Some name",
                                 "Some last name")
        self.assertEqual(response, {'message': 'validation_error'})
