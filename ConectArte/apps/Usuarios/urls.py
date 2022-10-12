from django.urls import path 
from .views import ProfileView,SearchArtist, EditProfile
app_name ="Usuarios"

urlpatterns = [
    path("<username>/",ProfileView.as_view(), name="perfil"),
    path("<username>/", SearchArtist.as_view(), name="search_results"),
    path('profile/edit', EditProfile, name="editProfile"),
    
]