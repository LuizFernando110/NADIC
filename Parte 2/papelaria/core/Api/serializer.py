from rest_framework import serializers
from core.models import Produto, Venda

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'nome', 'preco', 'marca', 'quantidade_em_estoque']

class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venda
        fields = ['id', 'produto', 'quantidade_da_compra', 'data_compra']