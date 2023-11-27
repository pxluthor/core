from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
import re


# Create your views here.
def bootstrap(request):
    return render (request,'exemplos/cadastro.html')


def validou_senha(senha):
    regex = '^(?=,*[A-Z])(?=,*[!#@$%&])(?=,*[0-9])(?=,*[a-z])(?=,*[A-Z]).{6,15}$'  
    if (re.search(regex, senha)):
        return True
    else:
        return False

def validou_email(email):
    regex = (r'^[a-x0-]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')  

    if (re.search(regex, email)):
        return True
    else:
        return False   

def validou_form(email, senha):
    if validou_email(email) and validou_senha(senha):
        return True
    else:
        return False     


def processa_formulario_v1(request):
    

    email = request.POST.get ("email")
    senha = request.POST.get ("senha")

    context = {
        'email' : email,
        'senha' : senha
    }

    if validou_form(email, senha):

        return HttpResponseRedirect ('/')
    else:
        return render(request, 'exemplos/cadastro.html', context)
                
    
