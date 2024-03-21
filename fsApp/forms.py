from django.contrib.auth.forms import UserCreationForm

from django import forms

from fsApp.models import Guest,User,incident,Persons,Addequipment

class DateInput(forms.DateInput):
    input_type = 'date'

class UserRegister(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label='password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='conform password',widget=forms.PasswordInput)


    class Meta:
        model = User
        fields = ('username','password1','password2')


class GuestRegister(forms.ModelForm):
    class Meta:
        model = Guest
        exclude = ("user",)


class Incident_register(forms.ModelForm):
    class Meta:
        model = incident
        fields = '__all__'


class AddnewPerson(forms.ModelForm):
    hire_date = forms.DateField(widget=DateInput)
    class Meta:
        model = Persons
        fields = '__all__'


class AddequipmentForm(forms.ModelForm):
    Purchase_Date = forms.DateField(widget=DateInput)
    Last_Maintenance_Date = forms.DateField(widget=DateInput)
    Next_Maintenance_Due = forms.DateField(widget=DateInput)
    Maintenance_Schedule = forms.DateField(widget=DateInput)
    Next_Inspection_Date = forms.DateField(widget=DateInput)



    class Meta:
        model = Addequipment
        fields =  '__all__'