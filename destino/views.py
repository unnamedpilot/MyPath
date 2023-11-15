from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from .models import MyRoutes

# Create your views here.
from .models import destino

def home(request):
    searchTerm=request.GET.get('searchDestino')
    destinos=destino.objects.all()
        
    return render(request,'home.html',{'searchTerm':searchTerm,'destinos':destinos})

def Mypaths(request):
    myroutes = MyRoutes.objects.all()
    return render(request,'mypaths.html',{'myroutes':myroutes})
