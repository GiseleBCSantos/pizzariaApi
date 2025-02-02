from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import *

class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        

class ItemPedidoSerializer(ModelSerializer):
    pizza_nome = serializers.CharField(source="id_pizza.sabor", read_only=True)
    tamanho_nome = serializers.CharField(source="id_tamanho.nome", read_only=True)
    preco_total = serializers.SerializerMethodField()

    class Meta:
        model = ItensPedido
        fields = ["id", "quantidade", "pizza_nome", "tamanho_nome", "preco_total"]

    def get_preco_total(self, obj):
        return obj.preco_item()
    
class ItemPedidoSerializerAdd(ModelSerializer):
    class Meta:
        model = ItensPedido
        fields = "__all__"
      
        
class PedidoSerializer(ModelSerializer):
    cliente_nome = serializers.SerializerMethodField()
    data_pedido = serializers.DateTimeField(format="%d/%m/%Y %H:%M", read_only=True)
    itens_pedidos = ItemPedidoSerializer(many=True, read_only=True)

    class Meta:
        model = Pedido
        fields = ["id", "data_pedido", "status", "valor_total", "cliente_nome", "itens_pedidos"]

    def get_cliente_nome(self, obj):
        return obj.cliente.nome
    
class PedidoSerializerAdd(ModelSerializer):
    class Meta:
        model = Pedido
        fields = "__all__"
        
class PizzaSerializer(ModelSerializer):
    class Meta:
        model = Pizza
        fields = '__all__'
  

class TamanhoSerializer(ModelSerializer):
    class Meta:
        model = Tamanho
        fields = '__all__'
        