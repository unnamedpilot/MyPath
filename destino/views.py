from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import destino

def home(request):
    searchTerm=request.GET.get('searchDestino')
    destinos=destino.objects.all()
        
    return render(request,'home.html',{'searchTerm':searchTerm,'destinos':destinos})
