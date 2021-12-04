from django.shortcuts import render

#acá importo las apps
from apps.productos.models import productos as product
from apps.usuarios.models import users as u


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

def users(request):

    usuarios = u.objects.all()

    context = {
        "usuarios" : usuarios 
    }

    return render(request,"login.html",context)
