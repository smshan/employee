from django.core import validators
from django.forms import ModelForm
from django import forms
from employee.models import employee,skills


class EmployeeRegistration(forms.ModelForm):
       class Meta:
                 model = employee
                 fields =['id','name','email','skill','roll']
                 widgets = {
                     'name':forms.TextInput(attrs={'class':'form-control', 'id':'nameid'}),
                     'email':forms.EmailInput(attrs={'class':'form-control','id':'emailid'}),
                   #  'skill':forms.SelectMultiple(attrs={'class':'form-select', 'id':'skillid'}),
                     'roll':forms.Select(attrs={'class':'form-select', 'id':'rollid'})
                 }



