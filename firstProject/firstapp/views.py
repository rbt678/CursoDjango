from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def display(request):
    return HttpResponse("<h1>Primeiro APP</h1>")

def displayDateTime(request):
    dt=datetime.datetime.now()
    s=f"<b>Dia e horas atual: {dt}</b>"
    return HttpResponse(s)