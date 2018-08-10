from datetime import datetime

import factory

from .models import Task


class TaskFactory(factory.django.DjangoModelFactory):
    status = Task.QUIUE
    create_time = datetime.now()
    start_time = None
    exec_time = None

    class Meta:
        model = 'tasks.Task'
