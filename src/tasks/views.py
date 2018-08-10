from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from tasks.tasks import task_for_task
from .models import Task
from .serializers import TaskSerializer, CreateTaskSerializer


class TaskView(CreateModelMixin, RetrieveModelMixin, GenericViewSet):
    serializer_class = CreateTaskSerializer
    queryset = Task.objects.all()

    def create(self, request, *args, **kwargs):
        task = Task.objects.create()
        task_for_task.delay(task.id)
        return Response({'id': task.id}, status=201)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = TaskSerializer(instance)
        return Response(serializer.data, status=200)
