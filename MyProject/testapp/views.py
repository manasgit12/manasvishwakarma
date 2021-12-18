from django.db import models
from django.db.models import fields
from django.shortcuts import render
from .models import Book
from .forms import Signupform
from django.contrib.auth.decorators import login_required
from django.views.generic import View,ListView,DetailView,UpdateView,DeleteView,CreateView
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy

class BookCreate(CreateView):
    model = Book
    fields = ('name','author','pages','price')
    success_url = reverse_lazy('book')

def home_view(request):
    books = Book.objects.all()
    return render(request,'testapp/home.html',{'book_list':books})

@login_required
def index_book(request):
    books = Book.objects.all()
    return render(request,'testapp/book_list.html',{'book_list':books})

class BookDetail(DetailView):
    model = Book

class Update_view(UpdateView):
   model = Book
   fields = ('name','price')
   success_url = reverse_lazy('book')

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('book')

def signup_info(request):
  form = Signupform()
  if request.method == 'POST':
    form = Signupform(request.POST)
    user = form.save()
    user.set_password(user.password)
    user.save()
    return HttpResponseRedirect('/accounts/login')
  return render(request,'testapp/signup.html',{'form':form})

  
def logout_view(request):
  return render(request,'testapp/logout.html')

@login_required
def about_view(request):
    return render(request,'testapp/about.html')



