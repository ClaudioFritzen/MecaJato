import re
from django.shortcuts import render
from django.http import HttpResponse

from .models import Clientes, Carro

# Create your views here.
def clientes(request):
    if request.method == "GET":
        return render(request, 'clientes.html')

    elif request.method == "POST":
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        
        #pegando uma lista
        carros = request.POST.getlist('carro')
        placas = request.POST.getlist('placa')
        ano = request.POST.getlist('ano')

        # Criando a validação para cpf
        cliente = Clientes.objects.filter(cpf = cpf)

        if cliente.exists():
           return render(request, 'clientes.html', {'nome': nome, 'sobrenome': sobrenome, 'email': email, 'carros': zip(carros, placas, ano)})
           #return HttpResponse('Cliente já existe')
        
        # validação de email
        
        if not re.fullmatch(re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'), email):
            return render(request, {'nome': nome, 'sobrenome': sobrenome, 'cpf': cpf, 'carros': zip(carros, placas, ano)})
            #return HttpResponse('email inválido')
                
        
        #pegando os dados que gostaria de salvar no banco
        cliente = Clientes(
            nome = nome,
            sobrenome = sobrenome,
            email = email,
            cpf = cpf
        )

        # salvando no banco
        cliente.save()

        # conhecendo o arquivo zip
       # x = list(zip(carros, placas, ano))
       # print(x)

        for carro, placa, ano in zip(carros, placas, ano):
            car = Carro(carros=carros, placas=placas, ano = ano, cliente = cliente)
            car.save()
            print(carro, placa, ano)
        return HttpResponse('Hello World!')