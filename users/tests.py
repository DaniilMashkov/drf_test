from rest_framework.test import APITestCase
from rest_framework import status
from users.models import CustomUser
from courses.models import Subscription


class CustomUserTestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser(email='aa@ss.ss', is_staff=True)
        self.user.set_password('Aa111111')
        self.user.save()

        response = self.client.post('/api/token/', {'email': 'aa@ss.ss', 'password': 'Aa111111'})
        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        self.test_data = {"email": "ee@ee.cc", "password": "Aa111111"}
        self.test_response_data = {"email": "aa@ss.ss", "avatar": None, "phone": None, "city": None}

    def test_create_user(self):
        response = self.client.post('/users/', self.test_data)

        self.assertEqual(response.json(), {"email": "ee@ee.cc", "avatar": None, "phone": None, "city": None})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_list_users(self):
        response = self.client.get('/users/')

        self.assertEqual(response.json(), [self.test_response_data])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user(self):
        response = self.client.get('/users/1/')

        self.assertEqual(response.json(), {
            'email': 'aa@ss.ss',
            'password': f'{self.user.password}',
            'avatar': None,
            'phone': None,
            'city': None,
            'payments': [],
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_destroy_user(self):
        response = self.client.delete('/users/1/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_retrieve_user(self):
        response = self.client.patch('/users/1/', {"city": "oops"})

        self.assertEqual(response.json(), {
            'email': 'aa@ss.ss',
            'password': f'{self.user.password}',
            'avatar': None,
            'phone': None,
            'city': 'oops',
            'payments': [],
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class SubscriptionTestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser(email='aa@ss.ss', is_staff=True)
        self.user.set_password('Aa111111')
        self.user.save()

        response = self.client.post('/api/token/', {'email': 'aa@ss.ss', 'password': 'Aa111111'})
        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        self.client.post('/courses/', {'name': 'any', 'description': '-'})
        self.test_data = {"course": 1, "status": True}

    def test_create_subscription(self):
        response = self.client.post('/users/subscriptions/', self.test_data)

        self.assertEqual(response.json(), self.test_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_list_subscriptions(self):
        self.client.post('/users/subscriptions/', self.test_data)
        response = self.client.get('/users/subscriptions/')

        self.assertEqual(response.json(), [self.test_data])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_subscription(self):
        self.client.post('/users/subscriptions/', self.test_data)
        response = self.client.get('/users/subscriptions/1/')

        self.assertEqual(response.json(), self.test_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_destroy_subscriptions(self):
        self.client.post('/users/subscriptions/', self.test_data)
        response = self.client.delete('/users/subscriptions/1/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_retrieve_subscription(self):
        self.client.post('/users/subscriptions/', self.test_data)
        response = self.client.patch('/users/subscriptions/1/', {"status": False})

        self.assertEqual(response.json(), {"course": 1, "status": False})
        self.assertEqual(response.status_code, status.HTTP_200_OK)