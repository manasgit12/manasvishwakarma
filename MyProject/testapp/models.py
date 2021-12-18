from django.db import models
from django.urls import reverse

# Create your models here.
 


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pages = models.PositiveIntegerField()
    price = models.IntegerField()
    

class Student():
    name = models.CharField(max_length=100)
    email = models.EmailField()

def get_absolute_url(self):
    return reverse("detail", kwargs={"pk": self.pk})

def __str__(self):
        return self.name

