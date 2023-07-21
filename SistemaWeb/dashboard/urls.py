from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('',views.inicio, name='inicio'),
    path('registro/', views.registro, name='registro'),
    path('clientes/', views.ClienteView.as_view(), name='cliente'),
    path('clientes/nuevo/', views.nuevo_cliente, name='nuevo_cliente'),
    path('vendedor/', views.VendedorView.as_view(), name='vendedor'),
    path('proformas/', views.ProformaView.as_view(), name='proforma'),
    path('proformas/agregar/', views.ProformaAgregarView.as_view(), name='agregar_proforma'),
    path('proformas/editar/<int:pk>/', views.ProformaEditarView.as_view(), name='editar_proforma'),
    path('proformas/eliminar/<int:pk>/', views.ProformaEliminarView.as_view(), name='eliminar_proforma'),
]