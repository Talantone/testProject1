from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from ..models import Task
from ..views import TasksAPIList


class TasksAPITestCase(APITestCase):
    def setUp(self):
        test_user1 = User.objects.create_user(username='test_user1', password='12345')
        test_user1.save()
        test_user2 = User.objects.create_user(username='test_user2', password='12345')
        test_user2.save()
        test_task = Task.objects.create(user=test_user2, task_text='Do something', status='u')
        test_task.save()
    def test_get_anonymous_users_tasks(self):
        url = reverse('tasks:my_tasks')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)
    def test_get_users_tasks(self):
        login1 = self.client.login(username='test_user1', password='12345')
        response = self.client.get(reverse('tasks:my_tasks'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.content), "b'[]'")
    def test_not_empty_users_tasks(self):
        login2 = self.client.login(username='test_user2', password='12345')
        response = self.client.get(reverse('tasks:my_tasks'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.content), 'b\'[{"task_text":"Do something","status":"u"}]\'')
