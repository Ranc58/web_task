from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
import logging
import django
from django.conf import settings


# logger = logging.getLogger("Celery")

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_task.settings')
os.environ['DJANGO_SETTINGS_MODULE'] = 'web_task.settings'

app = Celery('tasks')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
