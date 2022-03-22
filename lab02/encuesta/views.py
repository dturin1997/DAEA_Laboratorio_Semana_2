from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'titulo': "Formulario",
    }
    return render(request, 'encuesta/formulario.html', context)

def ejercicio1(request):
    context = {
        'titulo': "Operaciones Numericas",
    }
    return render(request, 'encuesta/formularioNumerico.html', context)

def enviar(request):
    context = {
        'titulo': "Respuesta",
        'nombre': request.POST['nombre'],
        'clave': request.POST['password'],
        'educacion': request.POST['educacion'],
        'nacionalidad': request.POST['nacionalidad'],
        'idiomas': request.POST.getlist('idiomas'),
        'correo': request.POST['email'],
        'website': request.POST['sitioweb'],
    }
    return render(request, 'encuesta/respuesta.html', context)

def calcular(request):
    context = {
        'titulo': "Resultado Ejemplo:",
        'num1': request.POST['num1'],
        'num2': request.POST['num2'],
        'operacion': request.POST['operacion'],
    }
    return render(request, 'encuesta/respuestaNumerica.html', context)