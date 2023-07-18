
def home(request):
    map = Map([{'latitude': 37.7829, 'longitude': -122.4190}])
    return render(request, 'home/home.html', {'map': map})