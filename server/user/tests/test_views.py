from django.test import TestCase


class TestUserRegisterView(TestCase):
    def test_user_registration(self):
        payload = {
            "email": "sample@email.com",
            "password": "samplepassword",
            "first_name": "Some name",
            "last_name": "Some last name"
        }

        response = self.client.post("/register", payload)
        self.assertEqual(response.status_code, 204)

    def test_user_invalid_data_raises_exception(self):
        payload = {
            "email": "sample@email.com",
            "first_name": "Some name",
            "last_name": "Some last name"
        }
        response = self.client.post("/register", payload)
        self.assertEqual(response.status_code, 400)
