from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)  # over writing password field

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'is_staff']
