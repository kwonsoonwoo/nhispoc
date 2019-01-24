import sys

from django.core.management import call_command
from django.db import models


class Data(models.Model):
    content = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content

    def save(self, *args, **kwargs):
        super().save()
        sysout = sys.stdout
        sys.stdout = open('db.json', 'wt')
        command = call_command('dumpdata', 'api.data', indent=2)
        sys.stdout = sysout
        return command