from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Address


class AddressView(CreateView):

    model = Address
    fields = ['address']
    template_name = 'home.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mapbox_access_token'] = 'pk.eyJ1IjoibGVlc2FuNjQiLCJhIjoiY2xrNzduejE0MDV0dDNnbjR0cDVtNnc4ciJ9.nA8U773QrxdRkRZiw8TlnA'
        context['addresses'] = Address.objects.all()
        return context