from django.shortcuts import render
from supermarket.models import Producto

# Create your views here.

def saludo(request):
    return render(request, 'hola.html')


def productos(request):
    productos = Producto.objects.all()
    return render(request, 'producto.html', {'productos': productos})