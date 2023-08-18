from django import forms

class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome',max_length=100, min_length=3)
    email = forms.EmailField(label='E-mail')
    assunto = forms.CharField(label='Assunto')
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())