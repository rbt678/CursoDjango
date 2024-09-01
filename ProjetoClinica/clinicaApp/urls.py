"""
URL configuration for ProjetoClinica project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from clinicaApp.views import PacientesList, PacientesCreate, PacientesUpdate, PacientesDelete, addDadosClinicos, analizar
from django.urls import path

urlpatterns = [
    path('', PacientesList.as_view(), name='pacientes'),
    path('pacientes/novo/', PacientesCreate.as_view()),
    path('pacientes/<int:pk>/update/', PacientesUpdate.as_view()),
    path('pacientes/<int:pk>/delete/', PacientesDelete.as_view()),
    path('pacientes/<int:pk>/dadosclinicos/', addDadosClinicos),
    path('pacientes/<int:pk>/dadosclinicos/analise/', analizar),
]
