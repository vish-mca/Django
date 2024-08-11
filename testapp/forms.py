from django import forms 
from .models import Employee

class EmployeeForm(forms.ModelForm):
    name=forms.CharField()
    marks=forms.IntegerField()

    class Meta:
        model=Employee 
        fields="__all__"