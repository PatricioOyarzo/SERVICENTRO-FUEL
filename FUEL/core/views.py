from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import gasolina
from .forms import GasForm
from django.http.response import JsonResponse


# Create your views here.

def home(request):
    #return HttpResponse('core/home.html')
    return render(request,'core/home.html')

def Tgasolina(request):
    #obtener listado de carreras desde el Modelo
    gasolinas = gasolina.objects.all()

    #cargar listado en diccionario datos
    datos = {
        'gasolinas':gasolinas
    }
    #cargar diccionario datos en el request (Lo envía a template carreras.html)
    return render(request,'core/ventas.html',datos)



def actualizar_objeto(request, objeto_id):
    if request.method == 'POST' and request.is_ajax():
        valor = int(request.POST.get('valor'))
        objeto = gasolina.objects.get(id=objeto_id)
        objeto.atributo += valor
        objeto.save()
        return JsonResponse({'message': 'Objeto actualizado correctamente'})
    return JsonResponse({'error': 'Método de solicitud incorrecto o no es una solicitud AJAX'})