import json
from typing import Any, Dict
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from .models import Address
from .models import Note
from .models import Entrevistado
from .forms import NoteForm
from .forms import AddressForm
from .forms import EntForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from .filters import notefilter
import requests
from django.shortcuts import render

def geocode_address(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        tipo = request.POST.get('tipo')
        nombre = request.POST.get('nombre')
        if address:
            # Realiza una solicitud a la API de Geocoder de Google Maps
            api_key = 'AIzaSyCxYSTI4oEMH98Llk94-k5vSi0MonHjhhQ'
            base_url = 'https://maps.googleapis.com/maps/api/geocode/json'
            params = {'address': address, 'key': api_key}

            response = requests.get(base_url, params=params)
            data = response.json()

            if data['status'] == 'OK':
                # Obtiene la latitud y longitud de la respuesta de la API
                lati = data['results'][0]['geometry']['location']['lat']
                lngi = data['results'][0]['geometry']['location']['lng']

                # Crea una nueva instancia del modelo Location y guárdala en la base de datos
                location = Address.objects.create(address=address, lat=lati, long=lngi, tipo=tipo, nombre=nombre)
                location.save()
                messages.success(request, 'Ubicación agregada exitosamente')
                return HttpResponseRedirect('/addresses')
            else:
                messages.success(request, 'La ubicación no se pudo agregar, intente nuevamente')
                return HttpResponseRedirect('/addresses')


    return render(request, 'new_address.html')

@login_required
def addNote(request):
    success = ""
    submitted = False
    form = NoteForm
    notes = Note.objects.all()
    if(request.method == "POST"):
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nota agregada exitosamente')
            return HttpResponseRedirect('/home')

    else:
            nombre_apellido = f"{request.user.first_name} {request.user.last_name}"
            form = NoteForm(initial={'autor': nombre_apellido, 'user': request.user })
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
            'autor': nota.autor
        })
    return JsonResponse(data, safe=False)

def get_ubicaciones(request):
    ubics = Address.objects.all()
    data = []
    for ubic in ubics:
        url_detail_ubic = reverse('detail_ubic', kwargs={'ubic_id': ubic.pk})
        data.append({
            'lat': ubic.lat,
            'long': ubic.long,
            'nombre': ubic.nombre,
            'tipo': ubic.tipo,
            'address': ubic.address,
            'pk': ubic.pk,
            'url_detail': url_detail_ubic,
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
            return HttpResponseRedirect('/addresses.html')
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
            messages.success(response, 'Ubicacion agregada exitosamente')
            a.save()
            return HttpResponseRedirect('/addresses')

    else:
        form = AddressForm()
    return render(response, "new_address.html", {"formulario" : form})

@login_required
def get_ubics(request):
    elementos = Address.objects.all()
    return render(request, 'addresses.html', {'ubics': elementos})

def get_notas(request):
     elementos = Note.objects.all()
     filtro = notefilter(request.GET, queryset=elementos)
     elementos = filtro.qs
     user = request.user
     context = {'notes' : elementos, 'filtro' : filtro, 'user':user}
     return render(request, 'notes.html', context)

def update_note(request, note_id):
    nota = Note.objects.get(pk=note_id)
    form = NoteForm(request.POST or None, instance=nota)
    if form.is_valid():
        form.save()
        messages.success(request, 'Nota actualizada exitosamente')
        return HttpResponseRedirect('/notes')
    return render(request, 'update_nota.html', {'nota':nota, 'formu':form})



def get_notas2(request):
     elementos = Note.objects.all()
     context = {'notas' : elementos}
     return render(request, 'det_address.html', context) 

def detail_page(request, note_id):
    obj=get_object_or_404(Note,pk=note_id)
    return render(request, 'det_nota.html', {'obj':obj})

def detail_ubic(request, ubic_id):
    obj = get_object_or_404(Address,pk=ubic_id)
    notas = Note.objects.all()

    context = {'notas' : notas, 'obj' : obj}
    return render(request, 'det_address.html', context)


def delete_ubic(request, ubic_id):
        # Obtener la instancia del modelo basada en el ID
        instancia = Address.objects.get(pk=ubic_id)
        # Eliminar la instancia del modelo
        instancia.delete()
        messages.success(request, 'La ubicacion se ha eliminado exitosamente')
        return redirect('/addresses')

def delete_note(request, note_id):
        # Obtener la instancia del modelo basada en el ID
        instancia = Note.objects.get(pk=note_id)
        # Eliminar la instancia del modelo
        instancia.delete()
        messages.success(request, 'La nota se ha eliminado exitosamente')
        return redirect('/notes')