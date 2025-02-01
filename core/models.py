from django.db import models
from datetime import datetime


class Cliente(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50)
    telefone = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nome
    
    

class Pizza(models.Model):
    sabor = models.CharField(max_length=50)
    precoBase = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.sabor


class Tamanho(models.Model):
    nome = models.CharField(max_length=50)
    modificador = models.DecimalField(max_digits=4, decimal_places=2)  # Exemplo: 1.5 para pizza média
    
    def __str__(self):
        return self.nome
    
    
class Pedido(models.Model):
    STATUS_CHOICES = [
        ('aberto', 'Aberto'),
        ('finalizado', 'Finalizado'),
        ('cancelado', 'Cancelado'),
    ]
    
    cliente_pedido = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="pedidos")
    data_pedido = models.DateTimeField(default=datetime.now())
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='aberto')
    valor_total = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    
    def calcular_total(self):
        total = 0
        for item in self.itens_pedidos.all():
            print(item)
            print(item.preco_item())
            total += item.preco_item()
        print("qwsçoqwdk\n", total)
        self.valor_total = total
        self.save()
    
    def __str__(self):
        return f"Pedido {self.id} - {self.cliente_pedido.nome}"


class ItensPedido(models.Model):
    itensPedido_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name="itens_pedidos")
    quantidade = models.IntegerField()
    id_pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, related_name="pizza_itens_pedidos")
    id_tamanho = models.ForeignKey(Tamanho, on_delete=models.CASCADE, related_name="tamanho_itens_pedidos")
    
    def preco_item(self):
        return self.id_pizza.precoBase * self.id_tamanho.modificador * self.quantidade
    
    def __str__(self):
        return f"{self.quantidade} x {self.id_pizza.sabor} ({self.id_tamanho.nome})"
