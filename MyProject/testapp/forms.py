from django import forms
from django.db import models
from django.db.models import fields
from django.forms.models import ModelForm
from .models import Book
from django.contrib.auth.models import User

class Signupform(forms.ModelForm):
  class Meta:
    model = User 
    fields = ['username','password','email','first_name','last_name']

