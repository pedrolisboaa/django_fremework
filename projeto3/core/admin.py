from django.contrib import admin
from .models import Cargo, Servico, Time
# Register your models here.

@admin.register(Cargo)
class CargoAdmin(admin.ModelAdmin):
    list_display = ['cargo',]

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'icone']

@admin.register(Time)
class TimeAdmin(admin.ModelAdmin):
    list_display = ['nome']