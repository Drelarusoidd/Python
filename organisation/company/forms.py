from dataclasses import fields
from django.contrib.auth.models import User
from django import forms
from .models import Unit, Employee, Profile

class UserRegistration(forms.ModelForm):
    
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('full_name', 'position', 'department', 'start_work')
    
        widgets = {
            'start_work': forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={'class': 'form-control', 
                       'placeholder': 'Select a date',
                       'type': 'date'
                      }),
            }    

class UserLogIn(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class CreateUnit(forms.ModelForm):

    class Meta:
        model = Unit
        fields = ('unit',)

class CreateEmployee(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('full_name', 'position', 'department', 'start_work')

        widgets = {
            'start_work': forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={'class': 'form-control', 
                       'placeholder': 'Select a date',
                       'type': 'date'
                      }),
            }    

class UpdateDepartment(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('department',)