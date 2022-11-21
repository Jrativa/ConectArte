from django.views.generic import TemplateView, View
from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from apps.Usuarios.models import Usuario
from .forms import *
from .models import *

def is_valid_param(param):
        return param != '' and param is not None

# Create your views here.
class VacanteView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        userLoggedIn = request.user
        form = VacanteForm()
        Vacantes = Vacante.objects.all()

        cantante_cb = request.GET.get('cantante_cb')
        musico_cb = request.GET.get('musico_cb')
        animador_cb = request.GET.get('animador_cb')
        pintor_cb = request.GET.get('pintor_cb')
        artesano_cb = request.GET.get('artesano_cb')
        max_num = request.GET.get('filtro_maximo')
        min_num = request.GET.get('filtro_minimo')

        if is_valid_param(min_num):
            Vacantes = Vacantes.filter(Pago__gte=min_num)

        if is_valid_param(max_num):
            Vacantes = Vacantes.filter(Pago__lt=max_num)

        if cantante_cb == 'on':
            Vacantes = Vacantes.filter(CategoriaVacante_id=1)

        elif musico_cb == 'on':
            Vacantes = Vacantes.filter(CategoriaVacante_id=2)

        elif animador_cb == 'on':
            Vacantes = Vacantes.filter(CategoriaVacante_id=3)

        elif pintor_cb == 'on':
            Vacantes = Vacantes.filter(CategoriaVacante_id=4)

        elif artesano_cb == 'on':
            Vacantes = Vacantes.filter(CategoriaVacante_id=5)
            
        
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