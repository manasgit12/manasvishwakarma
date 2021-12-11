from django import forms
from django.db.models import fields
from A1.models import Employee

class EmployeeModel(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'