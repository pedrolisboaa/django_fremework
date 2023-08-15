from django.urls import path
from .views import index, contato, cliente

urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato, name='contato'),
    path('cliente/<int:id>', cliente, name='cliente')
]
