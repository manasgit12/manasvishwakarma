from django.shortcuts import render,redirect
from A1.models import Employee
from A1.forms import EmployeeModel
# Create your views here.

def retrieve_info(request):
    empl = Employee.objects.all()
    return render(request,'A1/index.html',{'empl':empl})

def create_info(request):
    form = EmployeeModel()
    if request.method =='POST':
        form = EmployeeModel(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'A1/insert.html',{'form':form})

def delete_info(request,id):
    emll = Employee.objects.get(id=id)
    emll.delete()
    return redirect('/')

def update_info(request,id):
    emll = Employee.objects.get(id=id)
    if request.method == 'POST':
        form = EmployeeModel(request.POST, instance=emll)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'A1/update.html',{'emll':emll})

