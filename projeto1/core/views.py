from django.shortcuts import render
from .models import Cliente, Produto

# Create your views here.
def index(request):

    todosProdutos = Produto.objects.all()

    context = {
       'produtos': todosProdutos
    }

    return render(request, 'index.html', context)

def contato(request):

    clientes = Cliente.objects.all()

    context = {
        'clientes': clientes,
    }
    return render(request, 'contato.html', context)

def cliente(request, id):
    cli = Cliente.objects.get(id=id)
    
    context = {
        'cliente': cli
    }
    return render(request, 'cliente.html', context)