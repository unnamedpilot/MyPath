from django.contrib import admin
from .models import destino
from .models import MyRoutes

# Register your models here.

admin.site.register(destino)
admin.site.register(MyRoutes)