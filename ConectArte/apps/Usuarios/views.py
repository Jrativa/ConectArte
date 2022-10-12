from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, View, ListView
from django.contrib.auth import get_user_model
from apps.Usuarios.models import *
from django.db.models import Q
from .forms import UserForm
from django.contrib.auth.decorators import login_required


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

        

    
#     def post(self, request, username, *args, **kwargs):
#         user = get_object_or_404(User, username=username)
#         perfilUsuario = perfil.objects.get(usuario=user)
#         form = UserForm(request.POST)
#         if form.is_valid():
#             form.save()
#         context={
#             'form' : form,
#             'user':user,
#             'perfil':perfilUsuario
#         }
#         return render(request, 'users/editProfile.html', context)
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

class SearchArtist(View):
    def get(self, request, *args, **kwargs):
        query = self.request.GET.get('query')
        perfiles = perfil.objects.filter(Q(user__username__icontains=query))
        context={
            'perfiles':perfiles
        }
        return render(request, 'pages/search.html', context)
    


class SearchResultsView(ListView):
    model = User
    template_name = 'search.html'
    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = User.objects.filter( 
            Q(name__icontains=query) | Q(state__icontains=query)
        )
        return object_list
