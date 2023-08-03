import django_filters
from .models import Note

class notefilter(django_filters.FilterSet):

    campo_asociado = django_filters.CharFilter(lookup_expr='icontains', field_name='ubic__tipo')

    class Meta:
        model = Note
        fields = ['autor','entrevista', 'entrevistado', 'campo_asociado']

    def __init__(self, *args, **kwargs):
       super(notefilter, self).__init__(*args, **kwargs)
       self.filters['campo_asociado'].label="Tipo de terreno"


