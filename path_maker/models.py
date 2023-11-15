from django.db import models


class MyRoutes(models.Model):
    description = models.CharField(max_length=100000)