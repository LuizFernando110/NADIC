from django import forms
from .models import Produto, Venda

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome','preco','marca', 'quantidade_em_estoque']
    
class ProdutoCompra(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['quantidade_da_compra']