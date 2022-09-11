from django.db import models
from apps.Usuarios.models import *

# Create your models here.
class CategoriaPublicacion(models.Model):
    IdCatePub = models.AutoField(primary_key=True)
    NombreCatPub = models.CharField(max_length=20, blank=False, null=False)
    def __str__(self):
        return self.NombreCatPub

class Publicacion(models.Model):
    IdPublicacion = models.AutoField(primary_key=True)
    IdUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    Titulo = models.CharField(max_length=30, blank=False, null=False,  verbose_name="Titulo")
    DescripcionPublicacion = models.TextField(blank=False, null=False,  verbose_name="Descripción de la publicación")
    Multimedia = models.BinaryField(blank=False, null=False)
    FechaPublicacion = models.DateField(blank=False, null=False)

class Comentarios(models.Model):
    IdComentario = models.AutoField(primary_key=True)
    IdUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    IdPublicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    Comentario = models.TextField(blank=False, null=False)
    FechaComment = models.DateField(blank=False, null=False)

class PerteneceACategoria(models.Model):
    IdPublicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    IdCatePub = models.ForeignKey(CategoriaPublicacion, on_delete=models.CASCADE)