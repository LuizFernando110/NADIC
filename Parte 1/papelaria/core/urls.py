from django.urls import path
from .views import home
from .views import cadastrarProduto
from .views import editarProduto
from .views import excluirProduto
from .views import comprarProduto
from .views import faturamento

urlpatterns = [
    path('', home, name='home'),
    path('cadastrar/', cadastrarProduto, name='cadastrar_produto'),
    path('editar/<int:pk>', editarProduto, name='editar_produto'),
    path('excluir/<int:pk>', excluirProduto, name='excluir_produto'),
    path('comprar/<int:pk>', comprarProduto, name='comprar_produto'),
    path('faturamento/',faturamento, name='faturamento'), 
]
