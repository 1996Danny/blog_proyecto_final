from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Categorias(models.Model):

    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Noticias(models.Model):

    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="noticias")
    categoria = models.ForeignKey(Categorias, on_delete=models.SET_NULL, null= True)
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    # Para utilizar ImageField instalar pillow(pip install pillow)
    # cambiar el nombre d ela ubicacion de None = imagenes/media/img
    imagen = models.ImageField(upload_to=None)
    fecha = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo

# class comentario()