from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView
from .serializers import *
from .models import *

# Create your views here.

class ListCreateClienteApiView(ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class RetrieveUpdateDestroyClienteApiView(RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class ListCreatePizzaApiView(ListCreateAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


class RetrieveUpdateDestroyPizzaApiView(RetrieveUpdateDestroyAPIView):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    
    
class ListCreateTamanhoApiView(ListCreateAPIView):
    queryset = Tamanho.objects.all()
    serializer_class = TamanhoSerializer


class RetrieveUpdateDestroyTamanhoApiView(RetrieveUpdateDestroyAPIView):
    queryset = Tamanho.objects.all()
    serializer_class = TamanhoSerializer
    
    
class ListPedidoApiView(ListAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer


class CreatePedidoApiView(CreateAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializerAdd


class RetrieveUpdateDestroyPedidoApiView(RetrieveUpdateDestroyAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

    # def perform_create(self, serializer):
    #     pedido = serializer.save()
    #     pedido.calcular_total()
    #     pedido.save()
        

class CreateItemPedidoApiView(CreateAPIView):
    queryset = ItensPedido.objects.all()
    serializer_class = ItemPedidoSerializerAdd

    
    def perform_create(self, serializer):
        item = serializer.save()
        item.pedido.calcular_total()
        item.incrementar_total()
        item.pedido.save()
    

class ListItemPedidoApiView(ListAPIView):
    queryset = ItensPedido.objects.all()
    serializer_class = ItemPedidoSerializer

    

class RetrieveUpdateDestroyItemPedidoApiView(RetrieveUpdateDestroyAPIView):
    queryset = ItensPedido.objects.all()
    serializer_class = ItemPedidoSerializer