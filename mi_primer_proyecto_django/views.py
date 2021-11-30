from django.shortcuts import render


def home(request):

    productos = [
        {"name": "computadora","price":20},
        {"name": "celular","price":123}
    ]

    usuario = {
        "username":"lucas",
        "surname":"ibañez"
    }

    context = {
        "usuario": usuario,
        "productos": productos
    }

    return render(request,"home.html",context)