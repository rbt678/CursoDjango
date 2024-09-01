from django import forms
from clinicaApp.models import Pacientes, DadosClinicos

class PacientesForm(forms.ModelForm):
    class Meta:
        model=Pacientes
        fields='__all__'
        
class DadosClinicosForm(forms.ModelForm):
    class Meta:
        model=DadosClinicos
        fields='__all__'