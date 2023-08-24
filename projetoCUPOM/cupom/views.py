from django.shortcuts import render
from .models import Cupons


# Create your views here.

def index(request):
    cpf = request.GET.get('cpf')
    cupons = None

    print(cpf)
    
    if cpf:
        cupons = Cupons.objects.filter(cpf=cpf)
        

    context = {
        'cupons': cupons
    }


    return render(request, 'index.html', context)
