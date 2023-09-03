from django.shortcuts import render
from .models import Servico, Time 

# Create your views here.
def index(request):

    conteudo = {
        'servico': Servico.objects.all(),
        'time' : Time.objects.all(),
    }

    return render(request, 'index.html', conteudo)


# ERROS
def error_404(request, exception):
    return render(request, '404.html', status=404)


def error_500(request):
    return render(request, '500.html', status=500)