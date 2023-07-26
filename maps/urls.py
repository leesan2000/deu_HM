from django.urls import path
#from .views import AddressView
from .views import AddNoteView
from . import views


urlpatterns = [
    #path('home', AddressView.as_view(), name='home'),
    path('home', views.addNote, name='home'),
    path('notes', AddNoteView.as_view(), name='notes'),
    path('new_address', views.create, name='create'),
    path('get_notas/', views.get_notas, name='get_notas'),
    path('addresses', views.get_ubics, name='get_ubics')
]