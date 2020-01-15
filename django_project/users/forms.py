"""
form that inherits from the user creation form

"""
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        """
        configuration settings. will affect the user model and with the fields we want and in what order we want
        it.
        """
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        """
        configuration settings. will affect the user model and with the fields we want and in what order we want
        it.
        """
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']