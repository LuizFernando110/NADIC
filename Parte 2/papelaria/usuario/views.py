from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import FormularioAutentificacaoForm

def login_usuario(request):
    if request.method == 'POST':
        form = FormularioAutentificacaoForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
    else:
        form = FormularioAutentificacaoForm(request)
    return render(request, 'login.html', {'form':form})