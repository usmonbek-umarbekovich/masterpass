from django.forms import ModelForm
from django.db.models import fields
from .models import PassGen
import string, random


class PassForm(ModelForm):
    class Meta:
        model = PassGen
        fields = ['site_name', 'password']
    
    def pass_gen(self, pass_length):
        chars = "!@#$%^&**()_+"
        numbers = '0123456789'
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        all_chars = chars + numbers + lowercase + uppercase

        password = ''
        for i in range(max(pass_length, 5)):
            password += random.choice(all_chars)
        print(password)
        return password

    def clean(self):
        self.cleaned_data['password'] = self.pass_gen(int(self.cleaned_data['password']))
    