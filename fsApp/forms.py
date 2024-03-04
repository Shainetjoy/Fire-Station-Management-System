from django.contrib.auth.forms import UserCreationForm

from django import forms

from fsApp.models import Guest,User


class UserRegister(UserCreationForm):
    Username = forms.CharField()
    Password = forms.CharField(label='password',widget=forms.PasswordInput)
    Password2 = forms.CharField(label='password',widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ('Username','Password','Password2')


class GuestRegister(forms.ModelForm):
    class Meta:
        model = Guest
        exclude = ("user",)