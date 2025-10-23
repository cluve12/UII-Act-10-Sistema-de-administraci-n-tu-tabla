from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agregar/', views.agregar_producto, name='agregar_producto'),
    path('editar/<int:id_producto>/', views.editar_producto, name='editar_producto'),
    path('eliminar/<int:id_producto>/', views.eliminar_producto, name='eliminar_producto'),
]