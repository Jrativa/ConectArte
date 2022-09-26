from django.urls import path 
from .views import ProfileView
app_name ="Usuarios"

urlpatterns = [
    path("users/<username>/",ProfileView.as_view(), name="perfil"),
]