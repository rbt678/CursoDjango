from django.shortcuts import render

# Create your views here.
def renderTemplate(request):
    dicionario = {'nome': 'Javier', 'idade': 27}
    return render(request, 'templatesApp/firstTemplate.html', context=dicionario)