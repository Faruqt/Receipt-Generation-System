from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class TestCreateGetReceipt(APITestCase):

	def authenticate(self):
		user_register_details= {"username":"Luffy", "password":"12345luf", "password2":"12345luf"}
		self.client.post(reverse('auth:auth_register'), user_register_details)

		user_login_details= {"username":"Luffy", "password":"12345luf"}
		response = self.client.post(reverse('auth:token_obtain_pair'), user_login_details )

		self.client.credentials(HTTP_AUTHORIZATION = f"Bearer {response.data['access']}")

	
	#test if unauthorized users can access reciept api endpoints
	#test create receipt endpoint
	def test_create_receipt_without_auth(self):
		sample_receipt = {"name":"Faruq", "address":"Wano Kingdom", "phone":"012345", "total_amount":2000}
		response= self.client.post(reverse('pdf:receipt'), sample_receipt) 
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

	#test get receipt endpoint
	def test_get_receipt_without_auth(self):
		response= self.client.get(reverse('pdf:receipt')) 
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

	#test get receipt set endpoint
	def test_get_receipt_set_without_auth(self):
		sample_receipt_id = str(2)
		response= self.client.get(reverse('pdf:receipt') +sample_receipt_id+'/') 
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

	#test authorized users access to reciept api endpoints
	def test_create_receipt(self):
		self.authenticate()
		sample_receipt = {"name":"Faruq", "address":"Wano Kingdom", "phone":"012345", "total_amount":2000}
		response= self.client.post(reverse('pdf:receipt'), sample_receipt) 
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

	def test_get_receipt(self):
		self.authenticate()
		response= self.client.get(reverse('pdf:receipt')) 
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_get_receipt_set(self):
		self.authenticate()
		sample_receipt_id = str(2)
		response= self.client.get(reverse('pdf:receipt') +sample_receipt_id+'/') 
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
