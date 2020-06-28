from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.authtoken.models import Token


class TestTodoListViews(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(email="sample@email.com",
                                                    first_name="First name",
                                                    last_name="Last name"
                                                    )
        token = Token.objects.create(user=self.user)
        self.token = f"Token {token}"

    def tearDown(self):
        Token.objects.all().delete()
        get_user_model().objects.all().delete()

    def test_todo_list_registration_payload(self):
        payload = {
            "list_name": "sample list name"
        }
        response = self.client.post("/list", payload, HTTP_AUTHORIZATION=self.token)
        self.assertEqual(response.status_code, 200)

    def test_todo_list_registration_with_no_name_fails(self):
        payload = {
            "foo": "bar"
        }
        response = self.client.post("/list", payload, HTTP_AUTHORIZATION=self.token)
        self.assertEqual(response.status_code, 400)

    def test_todo_list_deletion(self):
        payload = {
            "list_name": "foo"
        }
        response = self.client.post("/list", payload, HTTP_AUTHORIZATION=self.token)
        list_id = response.json()['id']
        response = self.client.delete(f'/list/{list_id}', HTTP_AUTHORIZATION=self.token)
        self.assertEqual(response.status_code, 204)

    def test_todo_list_item_add(self):
        payload = {
            "list_name": "foo"
        }
        response = self.client.post("/list", payload, HTTP_AUTHORIZATION=self.token)
        list_id = response.json()['id']
        response = self.client.post(f'/list/{list_id}', {"todo_item_name": "bar"},
                                    HTTP_AUTHORIZATION=self.token,
                                    content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_todo_list_item_update(self):
        response = self.client.post("/list", {"list_name": "foo"},
                                    HTTP_AUTHORIZATION=self.token,
                                    content_type='application/json')
        list_id = response.json()['id']
        response = self.client.post(f'/list/{list_id}', {"todo_item_name": "bar"},
                                    HTTP_AUTHORIZATION=self.token,
                                    content_type='application/json')
        item_id = response.json()['todo_item_id']
        response = self.client.put(f'/list/{list_id}/{item_id}', {"todo_item_name": "sub"},
                                   HTTP_AUTHORIZATION=self.token,
                                   content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_todo_list_item_delete(self):
        response = self.client.post("/list", {"list_name": "foo"},
                                    HTTP_AUTHORIZATION=self.token,
                                    content_type='application/json')
        list_id = response.json()['id']
        response = self.client.post(f'/list/{list_id}', {"todo_item_name": "bar"},
                                    HTTP_AUTHORIZATION=self.token,
                                    content_type='application/json')
        item_id = response.json()['todo_item_id']
        response = self.client.delete(f'/list/{list_id}/{item_id}',
                                   HTTP_AUTHORIZATION=self.token,
                                   content_type='application/json')
        self.assertEqual(response.status_code, 204)
