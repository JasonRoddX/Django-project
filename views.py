# Create your views here.
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
# from django.urls import reverse_lazy
from django.shortcuts import render
# from django.views.generic import TemplateView
# from django.views import generic
from conteos.models import Conteo
# from openpyxl import Workbook
# from django.http.response import HttpResponse

from imagenes.models import Imagen


def bienvenido(request):
    no_conteos_var = Conteo.objects.count()
    conteos = Conteo.objects.all()
    return render(request, 'bienvenido.html', {'no_conteos': no_conteos_var, 'conteos': conteos})


def imagenes(request):
    no_imagenes_var = Imagen.objects.count()
    imagenes = Imagen.objects.all()
    return render(request, 'imagenes.html', {'no_imagenes': no_imagenes_var, 'imagenes': imagenes})


def login(request):
    return render(request, 'index.html')


