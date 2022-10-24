from django import forms 
from .models import *

class PublicacionForm(forms.ModelForm):
    
    DescripcionPublicacion = forms.CharField(widget=forms.Textarea(attrs={
            'class':"form-control", 'id':"exampleFormControlTextarea1",
            'rows': '6',
            'placeholder': 'Escribe tu publicación:'
            }),
        required=True)
    
    Multimedia_Img = forms.FileField(widget=forms.ClearableFileInput(attrs={
        'class':"block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300 ",
        'multiple': True,
        'title':"uploadfile"
        }),
        required=True  
        )
    Multimedia_Video = forms.FileField(widget=forms.ClearableFileInput(attrs={
        'class':"block mb-2 text-sm font-medium text-gray-900 dark:text-gray-300 ",
        'multiple': True,
        'title':"uploadfile"
        }),
        required=False  
        )
    class Meta:
        model = Publicacion 
        fields = ['DescripcionPublicacion']