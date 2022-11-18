from django.db import models
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
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()