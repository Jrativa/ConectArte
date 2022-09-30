from django.views.generic import TemplateView, View
from django.shortcuts import redirect, render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from apps.Usuarios.models import Usuario
from .forms import *


class HomeView(View):
    def get(self, request, *args, **kwargs):
        
        context={

        }
        return render(request, 'pages/index.html', context)

@login_required
def home(request):
    return render(request, 'pages/home.html')

def prueba(request):
    return render(request, 'users/perfil.html')


# def finalSignup(request):
#     idActual = str(request.user.id)
#     o = Usuario.objects.raw("SELECT * from usuarios_usuario where IdTipoUsuario_id = "+idActual)
#     count = 0
#     for obj in o:
#         count += 1
#     return redirect(usuariosForm)