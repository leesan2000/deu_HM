import django_filters
from .models import Note
from django import forms


class notefilter(django_filters.FilterSet):

    campo_asociado = django_filters.CharFilter(lookup_expr='icontains', field_name='ubic__tipo')

    class Meta:
        model = Note
        fields = ['entrevista', 'campo_asociado']

        widgets = {
            
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'entrevista' : forms.TextInput(attrs={'class': 'form-control'}),
            'entrevistado' : forms.Select(attrs={'class':'form-control'}),
            'campo_asociado' : forms.TextInput(attrs={'class':'form-control'})
        }

    def __init__(self, *args, **kwargs):
       super(notefilter, self).__init__(*args, **kwargs)
       self.filters['campo_asociado'].label="Tipo de terreno"


