from django.urls import path
from . import views


app_name = "path"
urlpatterns = [
    path('', views.home, name = 'home'),
    path('path/', views.path_maker, name = 'path'),
    path('download_pdf/', views.download_pdf, name='download_pdf'),

]
