from django.views.generic import TemplateView, View
from django.shortcuts import redirect, render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from apps.Usuarios.models import Usuario
from apps.publicaciones.forms import *
from apps.publicaciones.models import *



class HomeView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        userLoggedIn = request.user
        form = PublicacionForm()
        posts = Publicacion.objects.all()

        context={
                'posts': posts,
                'form' : form,
            }
        return render(request, 'pages/home.html', context)
    
    def post(self, request, *args, **kwargs):
        userLoggedIn = request.user
        posts = Publicacion.objects.all()
        form = PublicacionForm(request.POST, request.FILES)
        files = request.FILES.getlist('Multimedia_Img')
        files2 = request.FILES.getlist('Multimedia_Video')
        
        if form.is_valid():
            newPost = form.save(commit=False)
            newPost.Autor = userLoggedIn
            newPost.save()
            for f in files:
                image = Imagen(imagen=f)
                image.save()
                newPost.Multimedia_Img.add(image)
            for f in files2:
                video = Video(video=f)
                video.save()
                newPost.Multimedia_Video.add(video)
            newPost.save() 
        context={
                'form' : form,
                'posts': posts,
            }
        return render(request, 'pages/home.html', context)
        

def home(request):
    context={
        }
    return render(request, 'pages/index.html', context)

