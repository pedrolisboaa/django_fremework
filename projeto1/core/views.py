from django.shortcuts import render

# Create your views here.
def index(request):

    context = {
        'chave': 'valor',
        'nome': 'Pedro Lisboa'
    }

    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')