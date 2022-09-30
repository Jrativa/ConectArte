from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView, View
from django.contrib.auth import get_user_model
from apps.Usuarios.models import *


User = get_user_model()

class ProfileView(View):
    def get(self, request, username, *args, **kwargs):
        user = get_object_or_404(User, username=username)
        perfilUsuario = perfil.objects.get(usuario=user)
        context={
            'user':user,
            'perfil':perfilUsuario
        }
        return render(request, 'users/perfilUsuario.html', context)
