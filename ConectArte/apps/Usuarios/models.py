from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import os 
from PIL import Image
from django.db.models.signals import post_save
from django.utils.text import slugify

# Create your models here.

def directorioUsuario(instancia, nombreArchivo):
    nombreFotoPerfil = "Usuarios/{0}/profile.jpg.".format(instancia.usuario.username)
    full_path = os.path.join(settings.MEDIA_ROOT, nombreFotoPerfil)
    if os.path.exists(full_path):
        os.remove(full_path)
    return nombreFotoPerfil 

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        perfil.objects.create(usuario=instance)

def guardarPerfil(sender, instance, **kwargs):
    instance.profile.save()

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



class Usuario(AbstractUser):
    IdUsuario = models.CharField(max_length=50)

    # def __str__(self):
    #     return self.NombreUsuario
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.NombreUsuario)
    #     super(Usuario, self).save(*args, **kwargs)
    # def getUserType(self):
    #     obj = Categorias.objects.get(IdCategoria = self.IdTipoUsuario)
    #     return obj.NombreCategoria

class perfil(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name="profile")
    fotoPerfil = models.ImageField(default="Usuarios/Usuario.png", upload_to=directorioUsuario)
    dateCreated = models.DateField(auto_now_add=True)
    Intereses = models.TextField(blank=False, null=True,  verbose_name="Intereses", default="")
    Educacion = models.TextField(blank=False, null=True,  verbose_name="Educacion", default="")
    Experiencia = models.TextField(blank=False, null=True,  verbose_name="Experiencia", default="")
    Descripcion = models.TextField(blank=False, null=True,  verbose_name="Descripción", default="")
    url = models.CharField(max_length=100, blank=False, null=False)
    NumeroTelefono = models.BigIntegerField(blank=True, null=True)
    def __str__(self):
        return self.usuario.username



post_save.connect(create_user_profile, sender=Usuario)
post_save.connect(guardarPerfil, sender=Usuario)


    

class ClasificaEn(models.Model):
    IdCategoria = models.ForeignKey(Categorias, on_delete=models.CASCADE, verbose_name="Categoria")
    IdUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Categoria")


# class Sigue(models.Model):
#     IdUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
#     SeguidoIdUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
