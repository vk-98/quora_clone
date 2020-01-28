from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    username = forms.CharField()

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']