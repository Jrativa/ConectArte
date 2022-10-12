from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, View, ListView
from django.contrib.auth import get_user_model
from apps.Usuarios.models import *
from django.db.models import Q


class SearchArtist(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('query')
        perfiles = perfil.objects.filter(Q(usuario__username__icontains=query))
        context={
            'perfiles':perfiles
        }
        return render(request, 'pages/search.html', context)

# Create your views here.
