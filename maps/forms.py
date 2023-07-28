from django import forms
from .models import Note
from .models import Address
from .models import Entrevistado

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = {'user', 'titulo', 'texto', 'ubic', 'entrevista', 'autor', 'tipo'}

        widgets = {
            
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'texto' : forms.Textarea(attrs={'class': 'form-control','rows':6,'cols':40,'style':'resize:none;'}),
            'ubic' : forms.Select(attrs={'class':'form-control'}),
            'entrevista' : forms.NullBooleanSelect(),
            'autor' : forms.TextInput(attrs={'class':'form-control'}),
            'tipo': forms.Select(attrs={'class':'form-control'})
        }

        labels = {
            'titulo': 'Titulo',
            'texto': 'Cuerpo',
            'ubic': 'Ubicacion',
            'entrevista': '¿Incluye una entrevista?',
            'autor': 'Autor',
            'tipo': 'Tipo de ubicacion'
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['user'].disabled = True

class AddressForm(forms.Form):
    address = forms.CharField(max_length=200)


class EntForm(forms.ModelForm):
    class Meta:
        model = Entrevistado
        fields = {'nombre', 'apellido', 'edad', 'profesion', 'fechaEntr'}
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'edad': 'Edad',
            'profesion': 'Profesion',
            'fechaEntr': 'Fecha de la entrevista'
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.TextInput(attrs={'class': 'form-control'}),
            'profesion': forms.TextInput(attrs={'class': 'form-control'}),
            'fechaEntr': forms.DateInput(attrs={'type': 'date'})
            }
        