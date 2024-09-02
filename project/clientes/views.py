from django.shortcuts import render


def index(request):
    nombre = "louis"
    apellido = "van bethoven"
    datos = {
        "nombre": nombre,
        "apellido": apellido,
    }
    return render(request, 'clientes/index.html', datos)
