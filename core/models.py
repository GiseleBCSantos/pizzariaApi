from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome
    
    

class Pizza(models.Model):
    sabor = models.CharField(max_length=50)
    precoBase = models.FloatField()
    
    def __str__(self):
        return self.sabor


class Tamanho(models.Model):
    nome = models.CharField(max_length=50)
    modificador = models.FloatField()
    
    def __str__(self):
        return self.nome
    
    
class Pedido(models.Model):
    cliente_pedido = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="pedidos")


class ItensPedido(models.Model):
    itensPedido_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name="itens_pedidos")
    quantidade = models.IntegerField()
    id_pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, related_name="pizza_itens_pedidos")
    id_tamanho = models.ForeignKey(Tamanho, on_delete=models.CASCADE, related_name="tamanho_itens_pedidos")