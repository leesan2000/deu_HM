from django.urls import path
from .views import AddressView


urlpatterns = [
    path('home', AddressView.as_view(), name='home'),
]