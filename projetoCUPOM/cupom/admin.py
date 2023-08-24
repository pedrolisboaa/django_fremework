from django.contrib import admin
from .models import Cupons

# Register your models here.

@admin.register(Cupons)
class CuponsAdmin(admin.ModelAdmin):
    list_display = ['cpf', 'numero_cupom', 'criado', 'modificado']