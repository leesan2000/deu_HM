from django import forms
from .models import Note
from .models import Address

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = {'user', 'titulo', 'texto', 'ubic', 'entrevistado', 'autor'}

        widgets = {
            
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'texto' : forms.Textarea(attrs={'class': 'form-control'}),
            'ubic' : forms.Select(attrs={'class':'form-control'}),
            'entrevistado' : forms.NullBooleanSelect(),
            'autor' : forms.TextInput(attrs={'class':'form-control'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['user'].disabled = True

class AddressForm(forms.ModelForm):
    model = Address
    fields = {'address'}
