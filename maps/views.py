from typing import Any, Dict
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import CreateView
from .models import Address
from .models import Note
from .models import Entrevistado
from .forms import NoteForm
from .forms import AddressForm
from .forms import EntForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect

@login_required
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

@login_required
def get_notas(request):
    notas = Note.objects.all()
    data = []
    for nota in notas:
        data.append({
            'lat': nota.ubic.lat,
            'long': nota.ubic.long,
            'titulo': nota.titulo,
            'texto': nota.texto,
            'nroVisita' : nota.nroVisita,
            'tipo' : nota.tipo,
            'autor': nota.autor
        })
    return JsonResponse(data, safe=False)

@login_required
def addEnt(request):
    submitted = False
    form2 = EntForm
    if(request.method == "POST"):
        form2 = EntForm(request.POST)
        if form2.is_valid():
            form2.save()
            return HttpResponseRedirect('/?submitted=True')

    else:
            form = EntForm()
            if 'submitted' in request.GET:
                submitted = True
    return render(request, 'new_ent.html', {'formEnt': form2, 'submitted':submitted})

class LoginRequiredMixin(LoginRequiredMixin):
    login_url = reverse_lazy('login')  # URL de la vista de inicio de sesión
    redirect_field_name = None

    def handle_no_permission(self):
        return redirect(self.login_url)


class AddNoteView(LoginRequiredMixin, CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes.html'
    success_url = '/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = Note.objects.all()
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

    return render(request, 'new_address.html', {'formAdd': form2})

@login_required
def create(response):
    if(response.method == "POST"):
        form = AddressForm(response.POST)
        if(form.is_valid()):
            ad = form.cleaned_data["address"]
            a = Address(address=ad)
            a.save()
    else:
        form = AddressForm()
    return render(response, "new_address.html", {"formulario" : form})

@login_required
def get_ubics(request):
    elementos = Address.objects.all()
    return render(request, 'addresses.html', {'ubics': elementos})
    