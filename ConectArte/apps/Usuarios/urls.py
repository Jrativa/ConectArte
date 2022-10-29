from django.urls import path 
from .views import ProfileView, EditProfile, followers
app_name ="Usuarios"

urlpatterns = [
    path("<username>/",ProfileView.as_view(), name="perfil"),
    path('profile/edit', EditProfile, name="editProfile"),
    #Se creó el nuevo path de followers
    path('profile/followers', followers, name="followers"),    
]