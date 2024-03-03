from django.contrib.auth.forms import UserCreationForm

from django import forms

from fsApp.models import Guest


class GuestRegister(UserCreationForm):
    Username = forms.CharField()
    Password = forms.CharField(label='password',widget=forms.PasswordInput)
    Password2 = forms.CharField(label='password',widget=forms.PasswordInput)


    class Meta:
        model = Guest
        fields = ('Username','Password','Password2')
