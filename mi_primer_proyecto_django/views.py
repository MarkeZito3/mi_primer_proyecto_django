from django.shortcuts import render
from django.views.generic import TemplateView 
#acá importo las apps
from apps.productos.models import productos as product
from apps.usuarios.models import users as u


#VIASTAS BASADAS EN FUNCIONES

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

    return render(request,"index.html",context)

def login(request):

    print(request.POST.get("username",None)," and ",request.POST.get("password",None))

    return render(request,"login.html",)



#VIASTAS BASADAS EN CLASES

"""
    detaileview: solo muestra un valor de la base de datos
    listview: listar todos los objetos de un modelo particular
    createview: crea un objeto
    updateview: actualiza un objeto
    delateview: borra un objeto

    estas son unas vistas que ya estan en django que ya tienen todo el código necesario para la
    cumplir con esas funcionalidades
"""


class Blog(TemplateView):
    template_name = "blog.html"
