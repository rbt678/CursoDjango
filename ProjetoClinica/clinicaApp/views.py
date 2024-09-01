from django.shortcuts import render, redirect
from clinicaApp.models import Pacientes, DadosClinicos
from clinicaApp.forms import DadosClinicosForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
class PacientesList(ListView):
    model = Pacientes
    
class PacientesCreate(CreateView):
    model = Pacientes
    success_url = reverse_lazy('pacientes')
    fields = ['nome', 'sobrenome', 'idade']

class PacientesUpdate(UpdateView):
    model = Pacientes
    success_url = reverse_lazy('pacientes')
    fields = ['nome', 'sobrenome', 'idade']

class PacientesDelete(DeleteView):
    model = Pacientes
    success_url = reverse_lazy('pacientes')
    
def addDadosClinicos(request, **kwargs):
    if request.method == 'POST':
        form = DadosClinicosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = DadosClinicosForm()
    paciente = Pacientes.objects.get(id=kwargs['pk'])
    return render(request, 'clinicaApp/dadosclinicos_form.html', {'form':form, 'paciente':paciente})

def analizar(request, **kwargs):
    dados = DadosClinicos.objects.filter(paciente=kwargs['pk'])
    dadosResposta=[]
    for entrada in dados:
        if entrada.procedimento == 'A/P':
            alturaePeso = entrada.resultado.split('/')
            if len(alturaePeso) == 2:
                BMI = float(alturaePeso[0])/((float(alturaePeso[1])/100)**2)
                bmiEntry = DadosClinicos()
                bmiEntry.procedimento = 'BMI'
                bmiEntry.resultado = BMI
                dadosResposta.append(bmiEntry)

        dadosResposta.append(entrada)
            
    return render(request, 'clinicaApp/analise.html', {'dados':dadosResposta})