from django.db import models
from django.utils import timezone

# Create your models here.
class PassGen(models.Model):
    site_name = models.CharField(max_length=200)
    password = models.CharField(max_length=300)
    time = models.DateTimeField(default=timezone.now)
    