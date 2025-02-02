
from django.urls import path
from .views import *

urlpatterns = [
    path("cliente/", ListCreateClienteApiView.as_view()),
    path("cliente/<int:pk>", RetrieveUpdateDestroyClienteApiView.as_view()),
    path("pizza/", ListCreatePizzaApiView.as_view()),
    path("pizza/<int:pk>", RetrieveUpdateDestroyPizzaApiView.as_view()),
    path("tamanho/", ListCreateTamanhoApiView.as_view()),
    path("tamanho/<int:pk>", RetrieveUpdateDestroyTamanhoApiView.as_view()),
    path("pedido/", ListPedidoApiView.as_view()),
    path("pedido/add/", CreatePedidoApiView.as_view()),
    path("pedido/<int:pk>", RetrieveUpdateDestroyPedidoApiView.as_view()),
    path("itempedido/", ListItemPedidoApiView.as_view()),
    path("itempedido/add/", CreateItemPedidoApiView.as_view()),
    path("itempedido/<int:pk>", RetrieveUpdateDestroyItemPedidoApiView.as_view()),
]
