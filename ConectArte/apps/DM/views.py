from django.shortcuts import render
from apps.DM.models import *

def mensajes_privados(request, username, *args, **kwargs):
    