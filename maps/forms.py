from django import forms
from .models import Note
from .models import Address
from .models import Entrevistado

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['user','titulo', 'texto', 'ubic', 'entrevista', 'fechaEntr', 'entrevistado', 'autor']

        widgets = {
            
            'user' : forms.HiddenInput(),
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'texto' : forms.Textarea(attrs={'class': 'form-control','rows':6,'cols':40,'style':'resize:none;'}),
            'ubic' : forms.Select(attrs={'class':'form-control'}),
            'fechaEntr' : forms.DateInput(attrs={'type': 'date', 'required': False}),
            'autor' : forms.TextInput(attrs={
                'class':'form-control',
                'readonly': 'readonly'}),
            'entrevistado': forms.Select(attrs={'class':'form-control'})
        }

        labels = {
            'titulo': 'Titulo',
            'texto': 'Cuerpo',
            'ubic': 'Ubicacion',
            'entrevista': '¿Incluye una entrevista?',
            'autor': 'Autor',
            'entrevistado': 'Persona entrevistada'
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)


class AddressForm(forms.ModelForm):
    class Meta:        
        model = Address
        fields = {'nombre', 'address', 'tipo'}

        widgets = {
            
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'address' : forms.Textarea(attrs={'class': 'form-control'}),
            'tipo' : forms.Select(attrs={'class':'form-control'}),
        }

        labels = {
            'nombre': 'Nombre',
            'address': 'Direccion',
            'tipo': 'Tipo de ubicación',
        }

    


class EntForm(forms.ModelForm):
    class Meta:
        model = Entrevistado
        fields = {'nombre', 'apellido', 'edad', 'profesion', 'fechaEntr'}
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'edad': 'Edad',
            'profesion': 'Profesion',
            'fechaEntr': 'Fecha de la entrevista',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.TextInput(attrs={'class': 'form-control'}),
            'profesion': forms.TextInput(attrs={'class': 'form-control'}),
            'fechaEntr': forms.DateInput(attrs={'type': 'date'})
        }
        