from django.db import models

# Create your models here.

class destino (models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='destino/images/')
    coordinates = models.CharField(max_length=50)

class MyRoutes(models.Model):
    description = models.CharField(max_length=100000)