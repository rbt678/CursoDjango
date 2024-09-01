from django.db import models

# Create your models here.
class Pacientes(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    idade = models.IntegerField()
    
class DadosClinicos(models.Model):
    PROCEDIMENTOS = [
        ('A/P', 'Altura/Peso'),
        ('FC', 'Frequencia Cardiaca'),
        ('P', 'Pressão'),
        ('T', 'Temperatura'),
    ]
    procedimento = models.CharField(choices=PROCEDIMENTOS, max_length=30)
    resultado = models.CharField(max_length=30)
    dataHora = models.DateTimeField(auto_now_add=True)
    paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)