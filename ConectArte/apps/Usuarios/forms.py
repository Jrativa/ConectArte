from django.db import models
from django.forms import ModelForm, TextInput,Textarea,Select
from apps.Usuarios.models import Usuario
from django import forms

from .models import perfil

class UserForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'shadow-sm focus:ring-indigo-500 dark:bg-dark-third dark:text-dark-txt focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md',
            })
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'shadow-sm focus:ring-indigo-500 dark:bg-dark-third dark:text-dark-txt focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md',
            })
    )
    Descripcion = forms.CharField(widget=forms.Textarea(attrs={
            'class':"form-control", 'id':"exampleFormControlTextarea1",
            'rows': '6',
            'placeholder': 'Escribe tu publicación:'
            }),
        required=True)
    
    Educacion = forms.CharField(widget=forms.Textarea(attrs={
        'class':"form-control", 'id':"exampleFormControlTextarea1",
        'rows': '6',
        'placeholder': 'Escribe tu publicación:'
        }),
    required=True)

    Experiencia = forms.CharField(widget=forms.Textarea(attrs={
        'class':"form-control", 'id':"exampleFormControlTextarea1",
        'rows': '6',
        'placeholder': 'Escribe tu publicación:'
        }),
    required=True)
    
    Intereses = forms.CharField(widget=forms.Textarea(attrs={
            'class':"form-control", 'id':"exampleFormControlTextarea1",
            'rows': '6',
            'placeholder': 'Escribe tu publicación:'
            }),
        required=True)
    
    url = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'shadow-sm focus:ring-indigo-500 dark:bg-dark-third dark:text-dark-txt focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md',
            })
    )
        
    
    NumeroTelefono = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'shadow-sm focus:ring-indigo-500 dark:bg-dark-third dark:text-dark-txt focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md',
            })
    )

    class Meta:
        model = perfil
        fields = ('Descripcion', 'Educacion','Experiencia','Intereses','url','NumeroTelefono')

