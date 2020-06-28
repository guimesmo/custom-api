import unittest
from unittest import mock

from common import TokenError
from todo_list import create_todo_list, view_todo_list, delete_todo_list,\
    add_list_item, update_list_item, delete_list_item
from . import mocks


class TestTodoListCreate(unittest.TestCase):
    @mock.patch("requests.post", return_value=mocks.MockSuccessResponse)
    @mock.patch("common.load_token", return_value="foo")
    def test_create_todo_list_must_return_the_list_payload(self, mock_res, mock_headers):
        response = create_todo_list("Sample Name")
        self.assertEqual(response, {"foo": "bar"})

    @mock.patch("common.load_token", return_value=None)
    def test_token_required_to_create_todo_list(self, mock_token):
        self.assertRaises(TokenError, create_todo_list, "Sample Name")

    @mock.patch("requests.get", return_value=mocks.MockSuccessResponse)
    @mock.patch("common.load_token", return_value="foo")
    def test_view_todo_list_must_return_payload(self, mock_token, mock_res):
        self.assertEqual(view_todo_list(1), {"foo": "bar"})

    @mock.patch("common.load_token", return_value="foobar")
    @mock.patch("requests.delete", return_value=mocks.MockNoContentResponse)
    def test_delete_todo_must_return_successfull_info(self, mock_token, mock_res):
        self.assertEqual(delete_todo_list(1), "Deleted successfully")

    @mock.patch("common.load_token", return_value="foobar")
    @mock.patch("requests.delete", return_value=mocks.MockNotFoundResponse)
    def test_delete_todo_must_response_error_on_not_found(self, mock_token, mock_res):
        self.assertEqual(delete_todo_list(1), {'message': 'not found'})

    @mock.patch("common.load_token", return_value="foobar")
    @mock.patch("requests.post", return_value=mocks.MockSuccessResponse)
    def test_add_todo_item_must_response_item_payload(self, mock_token, mock_res):
        self.assertEqual(add_list_item(1, 1), {'foo': 'bar'})

    @mock.patch("common.load_token", return_value="foobar")
    @mock.patch("requests.delete", return_value=mocks.MockNoContentResponse)
    def test_delete_list_item_must_return_successfull_info(self, mock_token, mock_res):
        self.assertEqual(delete_list_item(1, 1), "Deleted successfully")

    @mock.patch("common.load_token", return_value="foobar")
    @mock.patch("requests.delete", return_value=mocks.MockNotFoundResponse)
    def test_delete_list_item_must_response_error_on_not_found(self, mock_token, mock_res):
        self.assertEqual(delete_list_item(1, 1), {'message': 'not found'})

    @mock.patch("common.load_token", return_value="foobar")
    @mock.patch("requests.put", return_value=mocks.MockSuccessResponse)
    def test_update_list_item_must_response_item_payload_on_success(self, mock_token, mock_res):
        self.assertEqual(update_list_item(1, 1, 'sample item'), {'foo': 'bar'})
