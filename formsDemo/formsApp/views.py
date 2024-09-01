from django.shortcuts import render
from formsApp.models import Employee
from . import forms
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def userRegistrationView(request):
    form=forms.UserRegistrationForm()
    if request.method=='POST':
        form=forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'formsDemo/userRegistration.html', {'form':form})

@login_required
def principalView(request):
    return render(request, 'formsDemo/principal.html')

@login_required
def consultaView(request):
    context={'empregados': Employee.objects.all()}
    return render(request, 'formsDemo/consultar.html', context)

@login_required
def adicionarView(request):
    context = {'form': forms.EmpregadoForm()}
    if request.method=='POST':
        form=forms.EmpregadoForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'formsDemo/adicionar.html', context)