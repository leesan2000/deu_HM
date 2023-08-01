from django.urls import path
#from .views import AddressView
from .views import AddNoteView
from . import views


urlpatterns = [
    #path('home', AddressView.as_view(), name='home'),
    path('home/', views.addNote, name='home'),
    path('notes/', AddNoteView.as_view(), name='notes'),
    path('new_address/', views.create, name='create'),
    path('get_ubicaciones/', views.get_ubicaciones, name='get_ubicaciones'),
    path('addresses/', views.get_ubics, name='get_ubics'),
    path('new_ent/', views.addEnt, name='createEnt'),
    path('notes/<int:note_id>', views.detail_page, name='detail'),
    path('profile/', views.profile, name='profile'),
    path('delete_ubic/<int:ubic_id>/', views.delete_ubic, name='delete_ubic'),
    path('delete_note/<int:note_id>/', views.delete_note, name='delete_note'),

]