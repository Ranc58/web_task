from __future__ import absolute_import, unicode_literals

import time
import random
from datetime import datetime

from web_task.celery import app
from .models import Task


@app.task
def task_for_task(id):
    task = Task.objects.get(id=id)
    task.start_time = datetime.now()
    task.save()
    time.sleep(random.randint(0, 10))
    task.time_to_execute = datetime.now()
    task.save()
