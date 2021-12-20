from django import forms
from django.forms import fields
from .models import Customer


class CustomersForm(forms.ModelForm):
    
    class Meta:
        model = Customer
        fields = ['email', 'name', 'interior', 'logo', 'graphic']