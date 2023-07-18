from django.shortcuts import render
from django.http import HttpResponse
from mapkick.django import Map
from ..maps.models import Address


def landing(request):
    return render(request, 'landingPage.html')

def home(request):
    map = Map([{'latitude': 37.7829, 'longitude': -122.4190}])
    return render(request, 'home/home.html', {'map': map})