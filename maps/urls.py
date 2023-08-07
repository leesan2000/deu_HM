from django.urls import path
#from .views import AddressView
from .views import AddNoteView
from . import views
from users.views import profile, edit_user


urlpatterns = [
    #path('home', AddressView.as_view(), name='home'),
    path('home/', views.addNote, name='home'),
    path('notes/', views.get_notas, name='notes'),
    path('new_address/', views.geocode_address, name='geocode_address'),
    path('get_ubicaciones/', views.get_ubicaciones, name='get_ubicaciones'),
    path('addresses/', views.get_ubics, name='get_ubics'),
    path('new_ent/', views.addEnt, name='createEnt'),
    path('notes/<int:note_id>', views.detail_page, name='detail_note'),
    path('addresses/<int:ubic_id>', views.detail_ubic, name='detail_ubic'),
    path('profile/', profile, name='profile'),
    path('editar/', edit_user, name='edit_user'),
    path('delete_ubic/<int:ubic_id>/', views.delete_ubic, name='delete_ubic'),
    path('delete_note/<int:note_id>/', views.delete_note, name='delete_note'),
    path('update_note/<int:note_id>/', views.update_note, name='update_note'),
    path('update_ubic/<int:ubic_id>/', views.update_ubic, name='update_ubic'),
    #path('geocode/', views.geocode_address, name='geocode_address'),


]