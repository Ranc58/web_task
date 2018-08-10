import json

from rest_framework import status
from rest_framework.test import APITestCase
from .models import Task
from .factories import TaskFactory


class TestTaskHandler(APITestCase):

    def setUp(self):
        self.task_url = '/a/v1/tasks/'

    def test_create_task(self):
        response = self.client.post(self.task_url)
        data = json.loads(response.content.decode())
        created_task_from_db = Task.objects.get(id=data['id'])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(created_task_from_db)

    def test_retrieve_task(self):
        task = TaskFactory()
        url_for_response = '{}{}/'.format(
            self.task_url,
            task.id
        )
        response = self.client.get(url_for_response)
        data = json.loads(response.content.decode())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            data['create_time'],
            task.create_time.strftime("%Y-%m-%dT%H:%M:%S")
        )
