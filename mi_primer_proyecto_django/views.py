from django.shortcuts import render
from apps.productos.models import productos as product


def home(request):

    productos = product.objects.all()

    usuario = {
        "username":"lucas",
        "surname":"ibañez"
    }

    context = {
        "usuario": usuario,
        "productos": productos
    }

    return render(request,"home.html",context)