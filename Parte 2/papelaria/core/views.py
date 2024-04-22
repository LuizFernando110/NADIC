from django.contrib.auth.decorators import login_required
from usuario.decorators import patrao_required

from django.shortcuts import render
from .models import Venda, Produto

@patrao_required
def faturamento(request):
    vendas = Venda.objects.order_by('-data_compra')
    
    faturamento_total = 0

    for venda in vendas:
        faturamento_total += venda.faturamento()

    return render(
        request, 
        'faturamento.html', 
        {
            'vendas':vendas, 
            'faturamento_total':faturamento_total,
        }
        )

@login_required
def home(request):
    produtos = Produto.objects.all()
    vendas = Venda.objects.all()
    return render(request, 'home.html', {'vendas':vendas,'produtos':produtos})