from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

class TestAuthentication(APITestCase):

    def test_authenticate(self):
        user_register_details= {"username":"Luffy", "password":"12345luf", "password2":"12345luf"}
        response = self.client.post(reverse('auth:auth_register'), user_register_details)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        user_login_details= {"username":"Luffy", "password":"12345luf"}
        response = self.client.post(reverse('auth:token_obtain_pair'), user_login_details )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    