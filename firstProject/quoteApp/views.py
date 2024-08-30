from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def displayQuote(request):
    return HttpResponse("O melhor investimento que podemos fazer é em nós mesmos.")