from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = {'titulo', 'texto','ubic'}

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'texto' : forms.Textarea(attrs={'class': 'form-control'}),
            'ubic' : forms.Select(attrs={'class':'form-control'}),
        }