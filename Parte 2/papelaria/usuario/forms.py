from django import forms
from django.contrib.auth.forms import AuthenticationForm

class FormularioAutentificacaoForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    username = forms.CharField(max_length=254, label='Nome do usuário ou e-mail')
    password = forms.CharField(label='Senha', strip=False, widget=forms.PasswordInput)
