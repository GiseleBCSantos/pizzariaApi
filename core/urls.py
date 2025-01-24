
from django.urls import path
from .views import *

urlpatterns = [
    path("cliente/", ListCreateClienteApiView.as_view()),
    path("pizza/", ListCreatePizzaApiView.as_view()),
    path("tamanho/", ListCreateTamanhoApiView.as_view()),
    path("pedido/", ListCreatePedidoApiView.as_view()),
    path("itempedido/", ListCreateItemPedidoApiView.as_view()),
]
