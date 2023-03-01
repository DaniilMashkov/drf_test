from rest_framework.test import APITestCase
from rest_framework import status
from users.models import CustomUser
from django.contrib.auth.models import Permission


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = CustomUser(email='aa@ss.ss', is_staff=True)
        self.user.set_password('Aa111111')
        self.user.save()
        permission = Permission.objects.get(name='Can change lesson')
        self.user.user_permissions.add(permission)
        self.user.save()

        response = self.client.post('/api/token/', {'email': 'aa@ss.ss', 'password': 'Aa111111'})

        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        self.client.post('/courses/', {'name': 'any', 'description': '-'})
        self.test_data = {"name": "111", "description": "-", "link": "https://youtube.com/ads", "course": 1}

        self.test_response_data = {"name": "111", "description": "-", "preview": None,
                                   "link": "https://youtube.com/ads", "course": 1}

    def test_create_lesson(self):
        response = self.client.post('/lessons/create/', self.test_data)

        self.assertEqual(response.json(), self.test_response_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_list_lessons(self):
        self.client.post('/lessons/create/', self.test_data)
        response = self.client.get('/lessons/')

        self.assertEqual(response.json(), [self.test_response_data])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_lesson(self):
        self.client.post('/lessons/create/', self.test_data)
        response = self.client.get('/lessons/1/')

        self.assertEqual(response.json(), self.test_response_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_destroy_course(self):
        self.client.post('/lessons/create/', self.test_data)
        response = self.client.delete('/lessons/delete/1/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_retrieve_course(self):
        self.client.post('/lessons/create/', self.test_data)
        response = self.client.patch('/lessons/1/', {
            "name": "111", "description": "+", "link": "https://youtube.com/ads", "course": 1})

        self.assertEqual(response.json(), {"name": "111", "description": "+", "preview": None,
                                           "link": "https://youtube.com/ads", "course": 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
