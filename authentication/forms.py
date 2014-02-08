'''
Created on Dec 11, 2013

@author: luka
'''
from django.forms.models import ModelForm
from django.contrib.auth.models import User
from django.forms.fields import CharField
from django.forms.util import ErrorList
from django.forms.forms import Form

class RegisterForm(ModelForm):
    password_retype = CharField(max_length=30, min_length=4, required=True)
    
    def is_valid(self):
        valid =super(RegisterForm, self).is_valid()
        
        if valid:
            if self.cleaned_data['password']!=self.cleaned_data['password_retype']:
                self.errors['password'] = ErrorList(['passwords don\'t match'])
                valid = False
            del self.cleaned_data['password_retype']
        
        return valid
    
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        
        
class LoginForm(Form):    
    username = CharField(max_length=25, min_length=4)
    password = CharField(max_length=25, min_length=4)
