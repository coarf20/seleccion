from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ClaseModelo(models.Model):
    nombre = models.CharField()
    apellido = models.CharField()
    tipoIdentificacion = models.CharField()
    numeroIdentificacion = models.IntegerField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    rol = models.BooleanField()

class Meta:
    abstract = True