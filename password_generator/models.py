from django.db import models
from django.utils import timezone

# Create your models here.
class PassGen(models.Model):
    site_name = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=300)
    created = models.DateTimeField(default=timezone.now)
    