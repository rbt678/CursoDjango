from django.shortcuts import render
from empApp.models import Employee

# Create your views here.
def dadosEmpregados(request):
    empregadosDict = {'empregados': Employee.objects.all()}
    return render(request, 'employees.html', empregadosDict)