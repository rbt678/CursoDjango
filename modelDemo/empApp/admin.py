from django.contrib import admin
from empApp.models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'salary', 'email')

admin.site.register(Employee, EmployeeAdmin)