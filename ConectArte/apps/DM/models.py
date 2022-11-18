from django.db import models
from django.db.models import Count
from django.conf import settings
import uuid

User = settings.AUTH_USER_MODEL

class ModelBase(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    tiempo = models.DateTimeField(auto_now_add=True)
    actualizar = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True




class CanalMensaje(ModelBase):
    canal = models.ForeignKey("Canal", on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()

class CanalUsuario(ModelBase):
    canal = models.ForeignKey("Canal",null=True, on_delete=models.SET_NULL)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

class CanalQuerySet(models.QuerySet):
    def solo_uno(self):
        return self.annotate(num_usuarios = Count("usuarios")).filter(num_usuarios=1)


    def solo_dos(self):
        return self.annotate(num_usuarios = Count("usuarios").filter(num_usuarios=2))


class CanalManager(models.Manager):
    
    def get_queryset(self, *args, **kwargs):
        return CanalQuerySet(self.model, using=self._db)


class Canal(ModelBase):
    usuarios = models.ManyToManyField(User, blank=True, through=CanalUsuario)
    objects = CanalManager()        