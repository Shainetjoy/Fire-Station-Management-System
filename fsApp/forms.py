from django.contrib.auth.forms import UserCreationForm

from django import forms

from fsApp.models import Guest,User


class UserRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='password',widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ('username','password1','password2')


class GuestRegister(forms.ModelForm):
    class Meta:
        model = Guest
        exclude = ("user",)