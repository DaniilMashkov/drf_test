from rest_framework.test import APITestCase
from rest_framework import status
from users.models import CustomUser
from django.contrib.auth.models import Permission


class CourseTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = CustomUser(email='aa@ss.ss', is_staff=True)
        self.user.set_password('Aa111111')
        self.user.save()
        permission = Permission.objects.get(name='Can change course')
        self.user.user_permissions.add(permission)
        self.user.save()

        response = self.client.post('/api/token/', {'email': 'aa@ss.ss', 'password': 'Aa111111'})

        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        self.test_data = {'name': 'any', 'description': '-'}
        self.test_response_data = {
            'name': 'any', 'description': '-', 'total_lessons_count': 0, 'lessons': [], 'is_subscribed': None
        }

    def test_create_course(self):
        response = self.client.post('/courses/', self.test_data)

        self.assertEqual(response.json(), self.test_response_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_list_course(self):
        self.client.post('/courses/', self.test_data)
        response = self.client.get('/courses/')

        self.assertEqual(response.json(), [self.test_response_data])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_course(self):
        self.client.post('/courses/', self.test_data)
        response = self.client.get('/courses/1/')

        self.assertEqual(response.json(), self.test_response_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_destroy_course(self):
        self.client.post('/courses/', self.test_data)
        response = self.client.delete('/courses/1/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_retrieve_course(self):
        self.client.post('/courses/', self.test_data)
        response = self.client.patch('/courses/1/', {'description': '+'})

        self.assertEqual(response.json(), {
            'name': 'any', 'description': '+', 'total_lessons_count': 0, 'lessons': [], 'is_subscribed': None
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
