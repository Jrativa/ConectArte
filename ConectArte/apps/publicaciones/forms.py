from django import forms 
from .models import *

class PublicacionForm(forms.ModelForm):
    DescripcionPublicacion = forms.CharField(widget=forms.Textarea(attrs={
            'class':"form-control", 'id':"exampleFormControlTextarea1",
            'rows': '6',
            'placeholder': 'Escribe tu publicación:'
            }),
        required=True)
    
    Multimedia = forms.FileField(widget=forms.ClearableFileInput(attrs={
        'class': 'relative dark:text-dark-txt dark:bg-dark-second cursor-pointer bg-white rounded-md font-medium text-indigo-600 hover:text-indigo-500 focus-within:outline-none focus-within:ring-2 focus-within:ring-offset-2 focus-within:ring-indigo-500',
        'multiple': True
        }),
        required=False
        )
    class Meta:
        model = Publicacion 
        fields = ['DescripcionPublicacion']