from django.shortcuts import render, redirect
from .utils.GPT import get_completion_automatic_format
from .utils.image import get_image_for_place
from .utils.pdf_utils import generate_pdf
from django.http import HttpResponse
from django.contrib import messages

from django.http import JsonResponse
from . import models as destino_models
from .models import MyRoutes

context = ""

def home(request):
    return render(request, 'path/home.html')

def path_maker(request):
    dato = request.POST.get('promptSpace')
    places_without_image = get_completion_automatic_format(dato)
    if places_without_image and len(places_without_image) > 0:
        settlement_position = len(places_without_image)-1
        settlement = places_without_image.pop(settlement_position)
        places = get_image_for_place(places_without_image, settlement)
        context = {'places':places}
        request.session['places'] = places
        return render(request, 'path/path.html', context)
    else:
        messages.error(request, "It's seems like the request is invalid, try to be a little more specific")
        return redirect('path:home')
    
def download_pdf(request):
    places = request.session.get('places')
    buffer = generate_pdf(places)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="informacion.pdf"'
    del request.session['places']
    return response

def add_routes(request):

    respuesta = request.session.get('places')
    print(respuesta)
        
    # Guardar la ruta en la base de datos (suponiendo que tienes un modelo MyRoutes)
    myroute = destino_models.MyRoutes(description=respuesta)
    myroute.save()

    return render(request,'path/mypaths.html',{'respuesta': respuesta})

    return JsonResponse({'mensaje': 'Error en la solicitud.'}, status=400)

def Mypaths(request):
    myroutes = MyRoutes.objects.all()
    return render(request,'path/mypaths.html',{'myroutes':myroutes})


