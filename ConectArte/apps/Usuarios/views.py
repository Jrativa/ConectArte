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


User = get_user_model()

#Vista para abrir la nueva pagina de followers
def followers(request):
    return render (request, 'users/followers.html')



class ProfileView(View):
    def get(self,  *args, **kwargs):
        user = get_object_or_404(User)
        perfilUsuario = perfil.objects.get(usuario=user)
        context={
            'user':user,
            'perfil':perfilUsuario
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