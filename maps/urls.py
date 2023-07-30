from django.urls import path
#from .views import AddressView
from .views import AddNoteView
from . import views


urlpatterns = [
    #path('home', AddressView.as_view(), name='home'),
    path('home/', views.addNote, name='home'), #Protegida
    path('notes/', AddNoteView.as_view(), name='notes'), #Protegida
    path('new_address/', views.create, name='create'), #Protegida
    path('get_notas/', views.get_notas, name='get_notas'), #Protegida
    path('addresses/', views.get_ubics, name='get_ubics'), #Protegida
    path('new_ent/', views.addEnt, name='createEnt'), #Protegida
]