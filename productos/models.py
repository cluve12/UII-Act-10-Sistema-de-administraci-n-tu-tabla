from django.db import models

class Producto(models.Model):
    TIPOS_PRODUCTO = [
        ('sandwich', 'Sandwich'),
        ('ensalada', 'Ensalada'),
        ('bebida', 'Bebida'),
        ('snack', 'Snack'),
        ('postre', 'Postre'),
    ]
    
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=20, choices=TIPOS_PRODUCTO)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    calorias = models.IntegerField()
    
    class Meta:
        db_table = 'productos'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
    
    def __str__(self):
        return f"{self.nombre} - ${self.precio}"