from django import forms
from .models import Users

class UserRegistration(forms.ModelForm):
        password = forms.CharField(widget=forms.PasswordInput)

        class Meta:
            model=Users
            fields = ['name','email','password']

class UserLogin(forms.ModelForm):
        password = forms.CharField(widget=forms.PasswordInput)

        class Meta:
            model=Users
            fields = ['email','password']
        