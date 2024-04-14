from django.shortcuts import render, get_object_or_404, redirect
from .models import Venda, Produto
from .forms import ProdutoForm, ProdutoCompra

def home(request):
    produtos = Produto.objects.all()
    return render(request, 'home.html', {'produtos':produtos})

def cadastrarProduto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProdutoForm()
    return render(request, 'cadastrar_produto.html', {'form':form})

def editarProduto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'editar_produto.html', {'form':form})

def excluirProduto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.delete()
        return redirect('home')
    return render(request, 'excluir_produto.html', {'produto':produto})

def comprarProduto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = ProdutoCompra(request.POST)
        if form.is_valid():
            quantidade_da_compra = form.cleaned_data['quantidade_da_compra']
            if quantidade_da_compra <= produto.quantidade_em_estoque:
                venda = Venda(produto=produto, quantidade_da_compra=quantidade_da_compra)
                venda.save()
                produto.compra(quantidade_da_compra)
                return redirect('home')
    else:
        form = ProdutoCompra()
    return render(request, 'comprar_produto.html', {'form': form, 'produto': produto})

def faturamento(request):
    vendas = Venda.objects.all()
    faturamento_total = 0
    for venda in vendas:
        valor_compra = venda.quantidade_da_compra * venda.produto.preco
        faturamento_total += valor_compra
        

    return render(request, 'faturamento.html',{'vendas':vendas, 'valor_compra':valor_compra, 'faturamento_total':faturamento_total})
