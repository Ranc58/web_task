from django.conf import settings
from rest_framework import serializers

from tasks.models import Task


class CreateTaskSerializer(serializers.Serializer):
    id = serializers.IntegerField()


class TaskSerializer(serializers.ModelSerializer):
    create_time = serializers.DateTimeField(format=settings.DATETIME_FORMAT)
    start_time = serializers.DateTimeField(format=settings.DATETIME_FORMAT)
    time_to_execute = serializers.DateTimeField(format=settings.DATETIME_FORMAT)

    class Meta:
        model = Task
        fields = (
            'status',
            'create_time',
            'start_time',
            'time_to_execute',
        )
