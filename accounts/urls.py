
from django.urls import path
from . import views


app_name = "accounts"
urlpatterns = [
    path('login/', views.login_views, name = 'login'),
    path('signup/', views.sign_up, name = 'sign_up'),
    path('logout/', views.logout_view, name='logout'),
    
]
    