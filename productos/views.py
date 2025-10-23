from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from django.contrib import messages

def index(request):
    productos = Producto.objects.all().order_by('tipo', 'nombre')
    return render(request, 'productos/index.html', {'productos': productos})

def agregar_producto(request):
    if request.method == 'POST':
        try:
            producto = Producto(
                nombre=request.POST['nombre'].strip().title(),
                tipo=request.POST['tipo'],
                precio=request.POST['precio'],
                calorias=request.POST['calorias']
            )
            producto.save()
            messages.success(request, '✅ Producto agregado correctamente!')
            return redirect('index')
            
        except Exception as e:
            return render(request, 'productos/agregar_producto.html', {
                'error': f'❌ Error al agregar producto: {str(e)}'
            })
    
    return render(request, 'productos/agregar_producto.html')

def editar_producto(request, id_producto):
    producto = get_object_or_404(Producto, id_producto=id_producto)
    
    if request.method == 'POST':
        try:
            producto.nombre = request.POST['nombre'].strip().title()
            producto.tipo = request.POST['tipo']
            producto.precio = request.POST['precio']
            producto.calorias = request.POST['calorias']
            producto.save()
            
            messages.success(request, '✅ Producto actualizado correctamente!')
            return redirect('index')
            
        except Exception as e:
            return render(request, 'productos/editar_producto.html', {
                'producto': producto,
                'error': f'❌ Error al actualizar producto: {str(e)}'
            })
    
    return render(request, 'productos/editar_producto.html', {'producto': producto})

def eliminar_producto(request, id_producto):
    producto = get_object_or_404(Producto, id_producto=id_producto)
    
    if request.method == 'POST':
        producto.delete()
        messages.success(request, '✅ Producto eliminado correctamente!')
        return redirect('index')
    
    return render(request, 'productos/eliminar_producto.html', {'producto': producto})