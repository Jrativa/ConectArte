from django.views.generic import TemplateView, View
from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from apps.Usuarios.models import Usuario
from .forms import *
from .models import *

# Create your views here.
class VacanteView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        userLoggedIn = request.user
        form = VacanteForm()
        Vacantes = Vacante.objects.all()
        context={
                'vacantes': Vacantes,
                'form' : form,
            }
        return render(request, 'pages/vacantes.html', context)
    
    def post(self, request, *args, **kwargs):
        userLoggedIn = request.user
        form = VacanteForm(request.POST)
        Vacantes = Vacante.objects.all()
        
        if form.is_valid():
            newVacante = form.save(commit=False)
            newVacante.AutorVacante = userLoggedIn
            newVacante.save()
        context={
                'form' : form,
                'vacantes': Vacantes,
            }
        return render(request, 'pages/vacantes.html', context)