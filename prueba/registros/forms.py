from django import forms
from .models import ComentarioContacto
from .models import Archivos
from django.forms import ModelForm, ClearableFileInput

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


class CustomClearableFileInput(ClearableFileInput):
    template_with_clear = '<br> <label> for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label> %(clear)s'


class FormArchivos(ModelForm):
    class Meta:
        model = Archivos
        fields = ['titulo', 'descripcion', 'archivo']
        widgets = {
            'archivo': CustomClearableFileInput
            }
        