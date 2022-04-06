from django.db import models
from django.utils import timezone


class ApacheAccessLog(models.Model):
    ip = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    data = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return '%s, %s' % (self.ip, self.date)