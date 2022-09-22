import email
from mailbox import NotEmptyError
from django.db import models

# Create your models here.
class Clientes(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    cpf = models.CharField(max_length=12)

    def __str__(self) -> str:
        return self.nome

class Carro(models.Model):
    carros = models.CharField(max_length=20)
    placas = models.CharField(max_length=20)
    ano = models.CharField(max_length=10)