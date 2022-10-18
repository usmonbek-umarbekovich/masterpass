from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class PassGen(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    site_name = models.CharField(max_length=200, unique=True)
    password = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.site_name

    class Meta:
        ordering = ['created']
    