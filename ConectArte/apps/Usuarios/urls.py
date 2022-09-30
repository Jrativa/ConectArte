from django.urls import path 
from .views import ProfileView
app_name ="Usuarios"

urlpatterns = [
    path("<username>/",ProfileView.as_view(), name="perfil"),
]