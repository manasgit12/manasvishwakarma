from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from A1.models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eno','ename','email','esal','eadd']

admin.site.register(Employee,EmployeeAdmin)
