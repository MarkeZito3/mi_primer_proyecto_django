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
    DetaileView: solo muestra un valor de la base de datos
    ListView: listar todos los objetos de un modelo particular
    CreateView: crea un objeto
    UpdateView: actualiza un objeto
    DelateView: borra un objeto
    TemplateView: solamente muestra un template

    estas son unas vistas que ya estan en django que ya tienen todo el código necesario
    para la cumplir con esas funcionalidades
"""


class Blog(TemplateView):
    template_name = "blog.html"

