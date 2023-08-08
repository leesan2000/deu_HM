import json
from typing import Any, Dict
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from .models import Address
from .models import Note
from .models import Entrevistado
from .forms import NoteForm, AddressForm, EntForm, EntrevistadoFormset
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
    user = request.user  # Obtén el usuario actual

    if request.method == "POST":
        form = NoteForm(request.POST, request.FILES)
        entrevistado_formset = EntrevistadoFormset(request.POST, prefix='entrevistado')

        if form.is_valid() and entrevistado_formset.is_valid():
            note = form.save(commit=False)  # No guardamos la nota aún
            note.user = user  # Asignamos el usuario actual al campo user

            print(form.cleaned_data['entrevista'])

            if form.cleaned_data['entrevista']:  # Verifica si el campo entrevista es verdadero
                print(entrevistado_formset.cleaned_data)
                if any(form.cleaned_data for form in entrevistado_formset):
                    note.save()  # Guarda la nota si el formulario de entrevistado tiene datos

                    entrevistados = entrevistado_formset.save(commit=False)
                    for entrevistado in entrevistados:
                        entrevistado.nota = note
                        entrevistado.save()

                    messages.success(request, 'Nota y entrevistados agregados exitosamente')
                    return HttpResponseRedirect('/home')
                else:
                    messages.warning(request, 'No completo los datos del entrevistado. Ingrese nuevamente a "Nueva Nota"...')
                    return render(request, 'home.html', {'form': form, 'entrevistado_formset': entrevistado_formset, 'submitted': submitted})
            else:
                note.save()
                messages.success(request, 'Nota agregada exitosamente')

            return HttpResponseRedirect('/home')
    else:
        form = NoteForm(initial={'user': user})
        entrevistado_formset = EntrevistadoFormset(prefix='entrevistado')

        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'home.html', {'form': form, 'entrevistado_formset': entrevistado_formset, 'submitted': submitted})

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
    nota = get_object_or_404(Note, pk=note_id)
    form = NoteForm(request.POST or None, instance=nota)
    entrevistado_formset = EntrevistadoFormset(request.POST or None, instance=nota, prefix='entrevistado')

    if form.is_valid() and entrevistado_formset.is_valid():
        form.save()
        entrevistado_formset.save()

        messages.success(request, 'Nota y entrevistados actualizados exitosamente')
        return HttpResponseRedirect('/notes')

    return render(request, 'update_nota.html', {'nota': nota, 'form': form, 'entrevistado_formset': entrevistado_formset})


def update_ubic(request, ubic_id):
    ubic = get_object_or_404(Address, pk=ubic_id)

    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        nombre = request.POST.get('nombre')
                # Crea una nueva instancia del modelo Location y guárdala en la base de datos
        ubic.tipo = tipo
        ubic.nombre = nombre
        ubic.save()
        messages.success(request, 'Ubicación actualizada exitosamente', {'ubic':ubic})
        return HttpResponseRedirect('/addresses')
    
    return render(request, 'update_ubic.html')



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