from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model


User = get_user_model()


class RegistrationTestCase(TestCase):
	def setUp(self):
		self.client = APIClient()
		self.url = reverse('register')

	def test_register_creates_user(self):
		payload = {
			'username': 'testuser',
			'email': 'test@example.com',
			'password': 'StrongPassw0rd!',
			'password2': 'StrongPassw0rd!'
		}
		response = self.client.post(self.url, payload, format='json')
		self.assertEqual(response.status_code, 201)
		# user exists in DB
		user = User.objects.filter(email=payload['email']).first()
		self.assertIsNotNone(user)
		self.assertEqual(user.username, payload['username'])
