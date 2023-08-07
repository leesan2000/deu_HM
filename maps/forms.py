from django import forms
from .models import Note
from .models import Address
from .models import Entrevistado
from bootstrap_datepicker_plus.widgets import DatePickerInput
from django.forms import inlineformset_factory

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['user','titulo', 'texto', 'ubic', 'entrevista', 'fechaEntr']

        widgets = {
            
            'user' : forms.HiddenInput(),
            'titulo': forms.TextInput(attrs={'placeholder':'Titulo de la nota','class': 'form-control'}),
            'texto' : forms.Textarea(attrs={'placeholder':'Cuerpo de la nota...','class': 'form-control','rows':5,'cols':40,'style':'resize:none;'}),
            'ubic' : forms.Select(attrs={'class':'form-control'}),
            'fechaEntr' : DatePickerInput(
                options={
                    "format": "DD/MM/YYYY", # moment date-time format
                    "showClose": True,
                    "showClear": True,
                    "showTodayButton": True,
                    "locale": "es",
                },
                attrs={'class': 'form-control'}
            ),
            'entrevista': forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)


class AddressForm(forms.ModelForm):
    class Meta:        
        model = Address
        fields = {'nombre', 'address', 'tipo'}

        widgets = {
            
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'address' : forms.TextInput(attrs={'class': 'form-control', 'id' : 'direccion', 'placeholder' : 'Ingrese una direccion'}),
            'tipo' : forms.Select(attrs={'class':'form-control'}),
        }

        labels = {
            'nombre': 'Nombre de la ubicación',
            'address': 'Dirección',
            'tipo': 'Tipo de ubicación',
        }

    


class EntForm(forms.ModelForm):
    class Meta:
        model = Entrevistado
        fields = {'nombre', 'apellido', 'edad', 'profesion'}
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'edad': 'Edad',
            'profesion': 'Profesion',
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.TextInput(attrs={'class': 'form-control'}),
            'profesion': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
EntrevistadoFormset = inlineformset_factory(
    parent_model=Note,  # Reemplaza 'Note' con el modelo principal de tus notas
    model=Entrevistado,
    fields=('nombre', 'apellido', 'edad', 'profesion'),
    widgets={
        'nombre': forms.TextInput(attrs={'class':'form-control'}),
        'apellido': forms.TextInput(attrs={'class': 'form-control'}),
        'edad': forms.TextInput(attrs={'class': 'form-control'}),
        'profesion': forms.TextInput(attrs={'class': 'form-control'}),
    },
    extra=1,  # El número de formularios vacíos que se muestran inicialmente
    can_delete=True,  # Permite eliminar formularios de entrevistados
)