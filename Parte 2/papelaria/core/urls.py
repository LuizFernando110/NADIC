from django.urls import path
from .Api.viewset import ProdutoListCreatAPIView, ProdutoRetriveUpdateDestroyAPIView, VendaListCreateAPIView,VendaRetriveUpdateDestroyAPIView
from .views import faturamento,home

urlpatterns = [
    path('', home, name='home'),
    path('LCProduto/',ProdutoListCreatAPIView.as_view(), name='LCProduto'),
    path('RUDProduto/<int:pk>/',ProdutoRetriveUpdateDestroyAPIView.as_view(), name='RUDProduto'),
    path('LCVenda/', VendaListCreateAPIView.as_view(), name='LCVenda'),
    path('RUDVenda/<int:pk>/', VendaRetriveUpdateDestroyAPIView.as_view(), name ='RUDVenda'),
    path('faturamento/', faturamento, name='faturamento'),
]
