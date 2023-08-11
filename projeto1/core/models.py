from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preco', decimal_places=2, max_digits=2)
    estoque = models.IntegerField('Quantidade em estoque')


class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=150)
    sobrenome = models.CharField('Sobrenome', max_length=150)
    email = models.EmailField('Email',)