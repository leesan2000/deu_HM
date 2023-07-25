from typing import Any, Dict
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Address
from .models import Note
from .forms import NoteForm


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
    return render(request, 'home.html', {'formu': form, 'submitted':submitted, 'notas' : notes})




    
    
    
class AddNoteView(CreateView):
    model = Note
    form_class = NoteForm
    template_name = 'notes.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = Note.objects.all()
        return context