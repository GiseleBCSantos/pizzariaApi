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
    
    
class ListCreatePedidoApiView(ListCreateAPIView):
    queryset = Pedido.objects.all()
    # serializer_class = PedidoSerializer

    def get_serializer_class(self):
        if self.request.method == "POST":
            return PedidoSerializerAdd
        return PedidoSerializer


class RetrieveUpdateDestroyPedidoApiView(RetrieveUpdateDestroyAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
        

class ListCreateItemPedidoApiView(ListCreateAPIView):
    queryset = ItensPedido.objects.all()
    # serializer_class = ItemPedidoSerializerAdd

    def get_serializer_class(self):
        if self.request.method == "POST":
            return ItemPedidoSerializerAdd
        return ItemPedidoSerializer
    
    def perform_create(self, serializer):
        item = serializer.save()
        item.pedido.calcular_total()
        item.incrementar_total()
        item.pedido.save()
    

class RetrieveUpdateDestroyItemPedidoApiView(RetrieveUpdateDestroyAPIView):
    queryset = ItensPedido.objects.all()
    serializer_class = ItemPedidoSerializer