from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Address
from .models import Note
from .forms import NoteForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class AddressView(LoginRequiredMixin,   CreateView):

    login_url = reverse_lazy('login')

    model = Address
    fields = ['address']
    template_name = 'home.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mapbox_access_token'] = 'pk.eyJ1IjoibGVlc2FuNjQiLCJhIjoiY2xrNzduejE0MDV0dDNnbjR0cDVtNnc4ciJ9.nA8U773QrxdRkRZiw8TlnA'
        context['addresses'] = Address.objects.all()
        return context

class AddNoteView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'add_note.html'
    #fields = '__all__'