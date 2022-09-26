from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView, View
from django.contrib.auth import get_user_model
from apps.Usuarios.models import perfil
User = get_user_model()

class ProfileView(View):
    def get(self, request, username, *args, **kwargs):
        user = get_object_or_404(User, username=username)
        perfil = perfil.objects.get(user=user)
        context={
            "user":user,
            "profile":perfil

        }
        return render(request, 'users/perfil.html', context)
