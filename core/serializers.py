from rest_framework.serializers import ModelSerializer
from .models import *

class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        
        
class PedidoSerializer(ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'
        
        
class PizzaSerializer(ModelSerializer):
    class Meta:
        model = Pizza
        fields = '__all__'
        

class ItemPedidoSerializer(ModelSerializer):
    class Meta:
        model = ItensPedido
        fields = '__all__'
        

class TamanhoSerializer(ModelSerializer):
    class Meta:
        model = Tamanho
        fields = '__all__'
        