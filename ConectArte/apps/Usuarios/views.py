from email import message
from multiprocessing import context
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, View, ListView
from django.contrib.auth import get_user_model
from requests import request
from apps.Usuarios.models import *
from django.db.models import Q
from .forms import UserForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


User = get_user_model()

#Vista para abrir la nueva pagina de followers
def followers(request):
    return render (request, 'users/followers.html')

def follow(request, username):
    IdUsuario = request.user.id
    IdUsuarioSeguido = get_object_or_404(User, username=username)
    UsuarioSeguido_id=IdUsuarioSeguido.id
    rel = SigueA(IdUsuario_id=IdUsuario, IdUsuarioSeguido_id=UsuarioSeguido_id )
    rel.save()
    messages.success(request, f'Ahora sigues a {username}')
    return render (request, 'pages/home.html')

def unfollow(request, username):
    IdUsuario = request.user
    IdUsuarioSeguido = get_object_or_404(User, username=username)
    UsuarioSeguido_id=IdUsuarioSeguido
    rel = SigueA.objects.filter(IdUsuario_id=IdUsuario, IdUsuarioSeguido_id=UsuarioSeguido_id ).get()
    rel.delete()
    messages.success(request, f'Ya no sigues a {username}')
    return render (request, 'pages/home.html')


class ProfileView(View):
    def get(self, request, username, *args, **kwargs):
        user = get_object_or_404(User, username=username)
        perfilUsuario = perfil.objects.get(usuario=user)
        proflogued = perfil.objects.get(usuario=request.user)
        context={
            'user':user,
            'perfil':perfilUsuario,
            'profreq':proflogued
        }
        return render(request, 'users/perfilUsuario.html', context)

@login_required
def EditProfile(request):
        user = request.user.id
        profile = perfil.objects.get(id=user)
        userInfo = User.objects.get(id=user)
        if request.method == 'POST':
            form=UserForm(request.POST, instance=profile)
            if form.is_valid():
                userInfo.first_name = form.cleaned_data.get('first_name')
                userInfo.last_name = form.cleaned_data.get('last_name')
                profile.Descripcion = form.cleaned_data.get('Descripcion')
                profile.Educacion = form.cleaned_data.get('Educacion')
                profile.Experiencia = form.cleaned_data.get('Experiencia')
                profile.Intereses = form.cleaned_data.get('Intereses')
                profile.url = form.cleaned_data.get('url')
                profile.NumeroTelefono = form.cleaned_data.get('NumeroTelefono')
                profile.save()
                userInfo.save()
                return redirect('users:perfil', username=request.user.username)
        else:
            form=UserForm(instance=profile)

        context={
            'form':form,
        }

        return render(request, 'users/editProfile.html', context)