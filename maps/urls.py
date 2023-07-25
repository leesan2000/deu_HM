from django.urls import path
#from .views import AddressView
from .views import AddNoteView
from . import views


urlpatterns = [
    #path('home', AddressView.as_view(), name='home'),
    path('home', views.addNote, name='home'),
    path('notes', AddNoteView.as_view(), name='notes'),



]