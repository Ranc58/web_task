from django.db import models
from django.utils.translation import ugettext_lazy as _


class Task(models.Model):

    QUIUE = 'in queue'
    RUN = 'run'
    COMPLETED = 'completed'

    STATUSES = (
        ('in queue', 'In Queue'),
        ('run', 'Run'),
        ('completed', 'Completed'),
    )

    status = models.CharField(max_length=25, choices=STATUSES, verbose_name=_('Status'), default=QUIUE)
    create_time = models.DateTimeField(verbose_name=_('Created'), auto_now_add=True)
    start_time = models.DateTimeField(verbose_name=_('Started'), null=True, blank=True, default=None)
    time_to_execute = models.DateTimeField(verbose_name=_('Executed'), null=True, blank=True, default=None)

    def save(self, *args, **kwargs):
        if self.time_to_execute:
            self.status = self.COMPLETED
        elif self.start_time:
            self.status = self.RUN
        super(Task, self).save(*args, **kwargs)
