from django.shortcuts import render
from django.contrib import messages
from .forms import ContatoForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contato(request):
    formulario = ContatoForm(request.POST or None)

    if str(request.method == 'POST'):
        if formulario.is_valid():
            formulario.enviar_email()
            
            """
            nome = formulario.cleaned_data['nome']
            email = formulario.cleaned_data['email']
            assunto = formulario.cleaned_data['assunto']
            mensagem = formulario.cleaned_data['mensagem']

            print(f'{nome} {email} {assunto} {mensagem}')
            """
            messages.success(request, 'Enviado com sucesso!')    
            formulario = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar.')

    contexto = {
        'formulario': formulario,
    }
    return render(request, 'contato.html', contexto)

def produto(request):
    return render(request, 'produto.html')