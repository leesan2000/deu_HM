from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import RegistrationForm
from faker import Faker
from .forms import CustomLoginForm
from django.conf import settings
from datetime import timedelta


# Create your views here.

def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            if request.user.is_authenticated:
                logout(request)

            user = form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)

            return redirect('/home')
    else:
        # Generar datos aleatorios con Faker para rellenar el formulario
        fake = Faker()
        fake_first_name = fake.first_name()
        fake_last_name = fake.last_name()
        fake_username = fake.user_name()
        fake_email = fake.email()
        fake_date_of_birth = fake.date_of_birth()
        fake_phone_number = fake.phone_number()
        fake_gender = fake.random_element(['H', 'M', 'O'])  

        # Crear un diccionario con los datos generados aleatoriamente
        random_data = {
            'first_name': fake_first_name,
            'last_name': fake_last_name,
            'username': fake_username,
            'email': fake_email,
            'password1': 'bocajuniors123',  
            'password2': 'bocajuniors123',  
            'date_of_birth': fake_date_of_birth,
            'phone_number': fake_phone_number,
            'gender': fake_gender,
        }

        # Crea el formulario con los datos generados aleatoriamente y pásalo a la plantilla
        form = RegistrationForm(random_data)

    return render(request, 'signup.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['usernameLogin']
            password = form.cleaned_data['password']
            remember_me = form.cleaned_data['remember_me']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if not remember_me:
                    request.session.set_expiry(0)
                else:
                    
                    request.session.set_expiry(settings.SESSION_COOKIE_AGE)
                return redirect('home')
            else:
                
                error_message = "Nombre de usuario o contraseña incorrectos."
                return render(request, 'login.html', {'form': form, 'error_message': error_message})
        else:
            
            return render(request, 'login.html', {'form': form})
    else:
        form = CustomLoginForm()
        return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('/')