from django.urls import path

from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('compra/', compra, name='compra'),
    path('vendedor/', vendedor, name='vendedor'),
    path('cliente/', cliente, name='cliente'),
    path('cliente_formulario/', cliente_formulario, name='cliente_formulario'),
    path('vendedor_formulario/', vendedor_formulario, name='vendedor_formulario'),
    path('compra_formulario', compra_formulario, name="compra_formulario"),
    path('busqueda_cliente/', busqueda_cliente, name='busqueda_cliente'),
    path('buscar/', buscar, name='buscar'),
 
]
