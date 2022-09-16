from django.shortcuts import render,HttpResponse

# Create your views here.
def clientes(request):
    return HttpResponse('Estou em clientes')