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
        data.append({
            'lat': ubic.lat,
            'long': ubic.long,
            'nombre': ubic.nombre,
            'tipo': ubic.tipo,
            'address': ubic.address
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


def detalle_objeto(request, note_id):
    objeto = get_object_or_404(Note, id=note_id)
    detalle_url = reverse('detalle_objeto', args=[note_id])
    return redirect(detalle_url)

def detail_page(request, note_id):
    obj=get_object_or_404(Note,pk=note_id)
    return render(request, 'det_nota.html', {'obj':obj})
        
@login_required
def profile(request):
    return render(request, 'profile.html')


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