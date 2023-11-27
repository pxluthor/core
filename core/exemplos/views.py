from django.shortcuts import render,HttpResponse

# Create your views here.
def bootstrap(request):
    return render (request,'exemplos/cadastro.html')

def processa_formulario_v1(request):
    #captar os dados digitados 
    return HttpResponse("recebeu a requisição via post")
