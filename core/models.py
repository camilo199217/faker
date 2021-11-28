import django
from django.db import models


class Credential(models.Model):
    created_at = models.DateTimeField(default=django.utils.timezone.now)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    ip = models.CharField(max_length=20)
