from typing import Any, Dict
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Address
from .models import Note
from .forms import NoteForm
from .forms import AddressForm


def addNote(request):
    submitted = False
    form = NoteForm
    notes = Note.objects.all()
    if(request.method == "POST"):
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/?submitted=True')

    else:
            form = NoteForm()
            if 'submitted' in request.GET:
                submitted = True
    return render(request, 'home.html', {'formu': form, 'submitted':submitted, 'notes' : notes})

def get_notas(request):
    notas = Note.objects.all()
    data = []
    for nota in notas:
        data.append({
            'lat': nota.ubic.lat,
            'long': nota.ubic.long,
            'titulo': nota.titulo,
            'texto': nota.texto,
        })
    return JsonResponse(data, safe=False)




    
    
    
class AddNoteView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = Note.objects.all()
        return context
    
class AddAddress(CreateView):
     model = Address
     form_class = AddressForm
     template_name = "addresses.html"

     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
     
     
def addAddress(request):
    form2 = AddressForm()
    if(request.method == "POST"):
        form2 = AddressForm(request.POST)
        if form2.is_valid():
            form2.save()
            return HttpResponseRedirect('/')
        else:
            form2 = AddressForm()

    return render(request, 'addresses.html', {'formAdd': form2})

def create(response):
    if(response.method == "POST"):
        form = AddressForm(response.POST)
        if(form.is_valid()):
            ad = form.cleaned_data["address"]
            a = Address(address=ad)
            a.save()
    else:
        form = AddressForm()
    return render(response, "addresses.html", {"formulario" : form})