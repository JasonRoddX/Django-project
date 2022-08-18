from django.db import models


# Create your models here.

class Imagen(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    id_mes = models.CharField(max_length=255)
    mesimagen = models.CharField(max_length=255)
    mesproceso = models.CharField(max_length=255)
    imagenesprocesadas = models.CharField(max_length=255)
    imagenesaprobadas = models.CharField(max_length=255)
    imagenesborradas = models.CharField(max_length=255)
    cantidausuario = models.CharField(max_length=255)
    promediousuario = models.CharField(max_length=255)
    promedioimagenes = models.CharField(max_length=255)
    porcentajeaprobadas = models.FloatField(max_length=255)
    porcentajeborradas = models.FloatField(max_length=255)
