from django import forms
from .models import ComentarioContacto

class ComentarioContactoForm(forms.ModelForm):
    class Meta:
        model = ComentarioContacto
        fields = ['usuario', 'mensaje']
        widgets = {
            'usuario': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su nombre',
                'required': 'required'
            }),
            'mensaje': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su mensaje',
                'rows': 5,
                'required': 'required'
            })
        }