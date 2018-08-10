from rest_framework import serializers

from tasks.models import Task


class CreateTaskSerializer(serializers.Serializer):
    id = serializers.IntegerField()


class TaskSerializer(serializers.ModelSerializer ):

    class Meta:
        model = Task
        fields = (
            'status',
            'create_time',
            'start_time',
            'time_to_execute',
        )
