from django.urls import path 
from .views import ProfileView, EditProfile
app_name ="Usuarios"

urlpatterns = [
    path("<username>/",ProfileView.as_view(), name="perfil"),
    path('profile/edit', EditProfile, name="editProfile"),
    
]