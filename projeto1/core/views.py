from django.shortcuts import render, get_object_or_404
from .models import Cliente, Produto

from django.http import HttpResponse
from django.template import loader

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
    #cli = Cliente.objects.get(id=id)
    # Isso aqui é pagina de ERRO IR EM URLS do principal, viws e no template

    cli = get_object_or_404(Cliente, id=id)
    
    
    context = {
        'cliente': cli
    }
    return render(request, 'cliente.html', context)

# VIEW DE ERROR
# Isso aqui é pagina de ERRO IR EM URLS do principal, viws e no template
def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type='text/html; charsetutf8', status=404)

def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charsetutf8', status=500)