# users/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    bio = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=True)
    profile_picture = forms.FileField(required=True)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'bio', 'profile_picture']


class CustomUserChangeForm(UserChangeForm):
    bio = forms.CharField(widget=forms.Textarea(attrs={'rows': 3}), required=False)
    profile_picture = forms.FileField(required=False)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'bio', 'profile_picture']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('password', None)
        self.fields.pop('username', None)

    def clean_username(self):
        return self.instance.username