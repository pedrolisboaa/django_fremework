from django.contrib import admin
from .models import Cliente, Produto

# Register your models here.

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')
    list_per_page = 20

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')
    list_per_page = 20