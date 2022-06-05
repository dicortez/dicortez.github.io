"""petfacha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import accesorios, camas, comida, correas, index, juguetes, register, login, chapas, ropa 
  

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', index,name="index"),
    path('index/', index,name="index"),
    path('register/',register,name="registrar-usuario"),
    path('login/',login,name="iniciar-sesion"),
    path('accesorios/',accesorios,name="accesorios"),
    path('camas/',camas,name="camas"),
    path('chapas/',chapas,name="chapas"),
    path('comida/',comida,name="comida-mascota"),
    path('correas/',correas,name="correas"),
    path('juguetes/',juguetes,name="juguetes"),
    path('ropa/',ropa,name="ropa-mascota"),


    
    
]
