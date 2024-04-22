from rest_framework import generics
from core.models import Produto, Venda
from .serializer import ProdutoSerializer, VendaSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.mixins import LoginRequiredMixin

class ProdutoListCreatAPIView(LoginRequiredMixin, generics.ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer    

class ProdutoRetriveUpdateDestroyAPIView(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class VendaListCreateAPIView(LoginRequiredMixin, generics.ListCreateAPIView):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer

    def create(self, request, *arg, **kwargs):
        quantidade_compra = request.data.get('quantidade_da_compra')
        produto_id = request.data.get('produto')

        try:
            produto = Produto.objects.get(pk=produto_id)
        except:
            return Response({"error": "Produto não encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
        if produto.compra(quantidade_compra):
            return super().create(request, *arg, **kwargs)
        else:
            return Response({"error": "Quantidade insuficiente em estoque"}, status=status.HTTP_400_BAD_REQUEST)


class VendaRetriveUpdateDestroyAPIView(LoginRequiredMixin, generics.RetrieveUpdateDestroyAPIView):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer

    def repor_item(self, venda):
        venda.produto.quantidade_em_estoque += venda.quantidade_da_compra
        venda.produto.save()
    
    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        
        self.repor_item(instance)
    
        return super().delete(request, *args, **kwargs)