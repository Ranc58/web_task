from __future__ import absolute_import, unicode_literals

import time
import random
from datetime import datetime
from django.utils import timezone
from web_task.celery import app
from .models import Task


@app.task
def task_for_task(id):
    task = Task.objects.get(id=id)
    task.start_time = datetime.now(tz=timezone.utc).time()
    task.save()
    time.sleep(random.randint(0, 10))
    task.exec_time = datetime.now(tz=timezone.utc).time()
    task.save()
