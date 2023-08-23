from django.db import models

# Create your models here.
class Base(models.Model):
    criado = models.DateField('Data de Criação',  auto_now_add=True)
    modificado = models.DateField('Data de modificação', auto_now=True)
    
    class Meta:
        abstract = True


class Cupons(Base):
    cpf = models.CharField('CPF', max_length=14)
    numero_cupom = models.CharField('Numero Cupom', max_length=5, unique=True)

    def __str__(self):
        return self.cpf