from email import message
from django.shortcuts import render
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

#create your views here.


def index(request):

    return render(request, 'petfacha/index.html')

def register(request):   

    return render(request, 'petfacha/registro.html')


def login(request):

    return render(request, 'petfacha/login.html')

def accesorios(request):

    return render(request, 'petfacha/accesorios.html')

def camas(request):

    return render(request, 'petfacha/camas.html')

def chapas(request):

    return render(request, 'petfacha/chapas.html')

def comida(request):

    return render(request, 'petfacha/comida.html')

def correas(request):

    return render(request, 'petfacha/correas.html')

def juguetes(request):

    return render(request, 'petfacha/juguetes.html')

def ropa(request):

    return render(request, 'petfacha/ropa.html')