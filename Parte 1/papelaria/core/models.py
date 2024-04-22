from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=150)
    preco = models.DecimalField(max_digits=5,decimal_places=2)
    marca = models.CharField(max_length=150)
    quantidade_em_estoque = models.IntegerField(null= True, default=None)

    def __str__(self):
        return self.nome
    
    def compra(self, quantidade_da_compra):
        if quantidade_da_compra <= self.quantidade_em_estoque:
            self.quantidade_em_estoque -= quantidade_da_compra
            self.save()
            return True
        else:
            return False

class Venda(models.Model):
    produto = models.ForeignKey(Produto,on_delete=models.CASCADE)
    quantidade_da_compra = models.IntegerField()
    data_compra = models.DateTimeField(auto_now=True)
