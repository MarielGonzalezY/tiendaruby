from django.shortcuts import render
from django.http import HttpResponse
from django.template import  Template, Context
from django.template import loader
from django.shortcuts import render
# Create your views here.
class Persona(object):
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido


def Neza(request):
    return render(request,'escuelaNeza.html')

def Morelos(request):
    return render(request,'morelos.html')


def Martin(request):
    return render(request,'martin.html')

def Home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def listEsc(request):
    return render(request,'listEsc.html')

def contacto(request):
    return render(request, 'contact.html')