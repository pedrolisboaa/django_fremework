from django.db import models

# Create your models here.

class Base(models.Model):
    criados = models.DateTimeField('Criação', auto_now_add=True)
    modificado = models.DateTimeField('Atualização', auto_now=True)

    class Meta:
        abstract = True


class Servico(Base):
    ICONE_OPCOES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Grafíco'),
        ('lni-users', 'Usuário'),
        ('lni-layers', 'UI/UX'),
        ('lni-mobile', 'Celular'),
        ('lni-rocket', 'Foguete'),
    )

    TITULO_OPCOES = (
        ('EASY TO USED', 'Fácil para usar'),
        ('AWESOME DESIGN', 'Design'),
        ('EASY TO CUSTOMIZE', 'Facil para costumizar'),
        ('UI/UX DESIGN', 'UI e UX'),
        ('APP DEVELOPMENT', 'Desenvolvimento de app'),
        ('USER FRIENDLY INTERFACE', 'Interface fácil'),
    )
    
    titulo = models.CharField('Título', max_length=30, choices=TITULO_OPCOES)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=12, choices=ICONE_OPCOES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
    
    def __str__(self):
        return self.titulo


class Cargo(Base):
    cargo = models.CharField('Cargo', max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str___(self):
        return self.cargo 

class Time(Base):
    nome = models.CharField('Nome', max_length=120)
    cargo = models.ForeignKey('core.Cargo', verbose_name='Cargo', on_delete=models.CASCADE)
    bio = models.CharField('Biografia', max_length=200)
    imagem = models.ImageField('Imagem', upload_to='equipe')

    class Meta:
        verbose_name = 'Time'
        verbose_name_plural = 'Galera'
    
    def __str__(self):
        return self.nome
