from django import forms
from .models import Note
from .models import Address

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = {'user', 'titulo', 'texto', 'ubic', 'entrevistado', 'autor', 'tipo'}

        widgets = {
            
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'texto' : forms.Textarea(attrs={'class': 'form-control','rows':6,'cols':40,'style':'resize:none;'}),
            'ubic' : forms.Select(attrs={'class':'form-control'}),
            'entrevistado' : forms.NullBooleanSelect(),
            'autor' : forms.TextInput(attrs={'class':'form-control'}),
            'tipo': forms.Select(attrs={'class':'form-control'})
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['user'].disabled = True

class AddressForm(forms.Form):
    direccion = forms.CharField(max_length=200)
