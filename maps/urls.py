from django.urls import path
from .views import AddressView
from .views import AddNoteView


urlpatterns = [
    path('home', AddressView.as_view(), name='home'),
    path('add', AddNoteView.as_view(), name='add'),
]