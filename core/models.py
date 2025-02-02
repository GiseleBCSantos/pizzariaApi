from django.db import models
# from datetime import datetime 
from django.utils.timezone import now


class Cliente(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)
    endereco = models.CharField(max_length=50, null=False, blank=False)
    telefone = models.CharField(max_length=50, null=False, blank=False)
    bairro = models.CharField(max_length=50, null=False, blank=False)
    
    def __str__(self):
        return self.nome
    
    

class Pizza(models.Model):
    sabor = models.CharField(max_length=50, null=False, blank=False)
    precoBase = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
    
    def __str__(self):
        return self.sabor


class Tamanho(models.Model):
    nome = models.CharField(max_length=50, null=False, blank=False)
    modificador = models.DecimalField(max_digits=4, decimal_places=2, null=False, blank=False)  # Exemplo: 0.5 para pizza média
    
    def __str__(self):
        return self.nome
    
    
class Pedido(models.Model):
    STATUS_CHOICES = [
        ('aberto', 'Aberto'),
        ('finalizado', 'Finalizado'),
        ('cancelado', 'Cancelado'),
    ]
    
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="pedidos", null=False, blank=False)
    data_pedido = models.DateTimeField(default=now, null=False, blank=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='aberto', null=False, blank=False)
    valor_total = models.DecimalField(max_digits=8, decimal_places=2, default=0.00, null=False, blank=False)
    
    def calcular_total(self):
        total = sum(item.preco_item() for item in self.itens_pedidos.all())
        self.valor_total = total
        self.save()

    
    def __str__(self):
        return f"Pedido {self.id} - {self.cliente_pedido.nome}"


class ItensPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name="itens_pedidos", null=False, blank=False)
    quantidade = models.IntegerField(null=False, blank=False)
    id_pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, related_name="pizza_itens_pedidos", null=False, blank=False)
    id_tamanho = models.ForeignKey(Tamanho, on_delete=models.CASCADE, related_name="tamanho_itens_pedidos", null=False, blank=False)
    
    def preco_item(self):
        return self.id_pizza.precoBase * self.id_tamanho.modificador * self.quantidade
    
    def incrementar_total(self):
        self.pedido.valor_total += self.preco_item()
    
    def __str__(self):
        return f"{self.quantidade} x {self.id_pizza.sabor} ({self.id_tamanho.nome})"
