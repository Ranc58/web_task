from django.conf import settings
from rest_framework import serializers

from tasks.models import Task


class CreateTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ()


class TaskSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format=settings.TIME_FORMAT)
    start_time = serializers.DateTimeField(format=settings.TIME_FORMAT)
    time_to_execute = serializers.DateTimeField(source='exec_time', format=settings.TIME_FORMAT)

    class Meta:
        model = Task
        fields = (
            'status',
            'create_time',
            'start_time',
            'time_to_execute',
        )
