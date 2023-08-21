from django.shortcuts import render
from django.contrib import messages
from .forms import ContatoForm, ProdutoModelForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

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

    if request.method == 'POST':
        # Aqui vai receber os dados + imagens, por isso o request.FILES
        formulario = ProdutoModelForm(request.POST, request.FILES)
        if formulario.is_valid():
            produto = formulario.save(commit=False)

            print(f'Nome - {produto.nome}')
            print(f'Preco - {produto.preco}')
            print(f'Estoque - {produto.estoque}')
            print(f'Imagem - {produto.imagem}')

            messages.success(request, 'Produtos enviados com sucesso.')
            formulario = ProdutoModelForm()
        else:
            messages.error(request, 'Erro ao salvar o produtpo')
    else:
        formulario = ProdutoModelForm()
    
    context = {
        'formulario': formulario
    }
    return render(request, 'produto.html', context)