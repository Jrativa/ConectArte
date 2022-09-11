from django.db import models
from django.utils.text import slugify

# Create your models here.

class TipoUsuario(models.Model):
    IdTipoUsuario = models.AutoField(primary_key=True )
    NombreTipoUsuario = models.CharField(max_length=30, blank=False, null=False )

    def __str__(self):
        return self.NombreTipoUsuario

class Categorias(models.Model):
    IdCategoria = models.AutoField(primary_key=True)
    NombreCategoria = models.CharField(max_length=20, blank=False, null=False)
    def __str__(self):
        return self.NombreCategoria

class Usuario(models.Model):
    IdUsuario = models.AutoField(primary_key=True)
    IdTipoUsuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE,verbose_name="Tipo de usuario")
    NombreUsuario = models.CharField(max_length=30, blank=False, null=False,  verbose_name="Nombre de usuario")
    Descripcion = models.TextField(blank=False, null=False,  verbose_name="Descripción")
    NumeroTelefono = models.IntegerField(blank=True, null=True)
    slug= models.SlugField(max_length=255, unique=True, default="default")

    def __str__(self):
        return self.NombreUsuario
    def save(self, *args, **kwargs):
        self.slug = slugify(self.NombreUsuario)
        super(Usuario, self).save(*args, **kwargs)
    def getUserType(self):
        obj = Categorias.objects.get(IdCategoria = self.IdTipoUsuario)
        return obj.NombreCategoria


class ClasificaEn(models.Model):
    IdCategoria = models.ForeignKey(Categorias, on_delete=models.CASCADE, verbose_name="Categoria")
    IdUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Categoria")


# class Sigue(models.Model):
#     IdUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
#     SeguidoIdUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
