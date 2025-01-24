from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .serializers import *
from .models import *

# Create your views here.

class ListCreateClienteApiView(ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    

class ListCreatePizzaApiView(ListCreateAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    
    
class ListCreateTamanhoApiView(ListCreateAPIView):
    queryset = Tamanho.objects.all()
    serializer_class = TamanhoSerializer
    
    
class ListCreatePedidoApiView(ListCreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    

class ListCreateItemPedidoApiView(ListCreateAPIView):
    queryset = ItensPedido.objects.all()
    serializer_class = ItemPedidoSerializer