from django.contrib import admin
from .models import Producto

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id_producto', 'nombre', 'tipo', 'precio', 'calorias')
    search_fields = ('nombre', 'tipo')
    list_filter = ('tipo',)
    list_editable = ('precio',)