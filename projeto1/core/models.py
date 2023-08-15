from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preco', decimal_places=2, max_digits=100)
    estoque = models.IntegerField('Quantidade em estoque')

    def __str__(self):
        return self.nome
    
    def calcular_valor_produtos(self):
        self.preco * self.estoque


class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=150)
    sobrenome = models.CharField('Sobrenome', max_length=150)
    email = models.EmailField('Email',)

    def __str__(self):
        return self.nome