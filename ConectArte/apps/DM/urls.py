from django.urls import path
from apps.DM.views import *


urlpatterns = [
    path("<str:username>", mensajes_privados)
]
