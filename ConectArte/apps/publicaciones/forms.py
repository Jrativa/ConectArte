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
        'class':"",
        'multiple': False,
        'placeholder': 'Agregar multimedia'
        }),
        required=False
        )
    class Meta:
        model = Publicacion 
        fields = ['DescripcionPublicacion']