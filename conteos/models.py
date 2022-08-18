from django.db import models


# Create your models here.
class Conteo(models.Model):
    # id = models.CharField(max_length=255, primary_key=True)
    SERVIDOR = models.CharField(max_length=255)
    CAMARA = models.CharField(max_length=255)
    MARZO = models.CharField(max_length=255)
    ABRIL = models.CharField(max_length=255)
    OTROS = models.CharField(max_length=255)
    VIDEOS = models.CharField(max_length=255)
    MULTAS = models.CharField(max_length=255)

#    return f'Conteo {self.id}: {self.SERVIDOR} {self.CAMARA} {self.NOVIEMBRE} {self.OTROS} {self.VIDEOS}'
