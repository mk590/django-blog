from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# click on the user creation form 

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    
    class Meta:
        model=User
        # fields='__all__'
        fields=['username', 'email', 'password1', 'password2']
    