from django.shortcuts import render,HttpResponse
from django.http import HttpResponseRedirect
import re


# Create your views here.
def bootstrap(request):
    return render (request,'exemplos/cadastro.html')


def validou_senha(senha):
    regex = (r'^(?=,*[A-Z])(?=,*[!#@$%&])(?=,*[0-9])(?=,*[a-z])(?=,*[A-Z]).{6,15}$')    
    if (re.search(regex, senha)):
        return True
    else:
        return False

def validou_email(email):
    regex = (r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')   
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
    # Captar os dados digitados 

    email = request.POST.get ("email")
    password = request.POST.get ("senha")

    if validou_form(email, password):

        return HttpResponseRedirect ("/")
    else:
        return render(request, 'exemplos/cadastro.html')
                
    
