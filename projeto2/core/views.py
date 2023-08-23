from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect

# Do forms eu uso para criar os formulários
from .forms import ContatoForm, ProdutoModelForm
# Do models para apresentar os dados
from .models import Produto

# Create your views here.
def index(request):
    conteudo = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'index.html', conteudo)

def contato(request):
    formulario = ContatoForm(request.POST or None)

    if request.method == 'POST':
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
    else:
        formulario = ContatoForm()

    contexto = {
        'formulario': formulario,
    }
    return render(request, 'contato.html', contexto)

def produto(request):
    if str(request.user) != 'AnonymousUser':
        if request.method == 'POST':
            # Aqui vai receber os dados + imagens, por isso o request.FILES
            formulario = ProdutoModelForm(request.POST, request.FILES)
            if formulario.is_valid():

                formulario.save()
                produto = formulario.save(commit=False)

                """
                print(f'Nome - {produto.nome}')
                print(f'Preco - {produto.preco}')
                print(f'Estoque - {produto.estoque}')
                print(f'Imagem - {produto.imagem}')
                """
                messages.success(request, 'Produtos enviados com sucesso.')
                formulario = ProdutoModelForm()
            else:
                messages.error(request, 'Erro ao salvar o produtpo')
        else:
            formulario = ProdutoModelForm()
    
        context = {
            'formulario': formulario
        }
    else:
        return redirect('index')

    return render(request, 'produto.html', context)