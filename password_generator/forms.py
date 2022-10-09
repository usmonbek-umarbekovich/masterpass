from django.forms import ModelForm
from django.db.models import fields
from .models import PassGen

class PassForm(ModelForm):
    class Meta:
        model = PassGen
        fields = ['site_name', 'password']