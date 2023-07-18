from django.shortcuts import render, redirect
from .forms import RegistrationForm
from faker import Faker

# Create your views here.

def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirect to a success page or do something else after successful registration
            return redirect('/')
    else:
        # Generar datos aleatorios con Faker para rellenar el formulario
        fake = Faker()
        fake_username = fake.user_name()
        fake_email = fake.email()
        fake_full_name = fake.name()
        fake_date_of_birth = fake.date_of_birth()
        fake_phone_number = fake.phone_number()
        fake_address = fake.address()
        fake_gender = fake.random_element(['M', 'F', 'O'])
        fake_profile_picture = None  # Puedes definir una imagen predeterminada o dejarla en blanco

        # Crear un diccionario con los datos generados aleatoriamente
        random_data = {
            'username': fake_username,
            'email': fake_email,
            'password1': 'password123',  # Puedes usar una contraseña predeterminada o generar una aleatoria
            'password2': 'password123',  # Asegúrate de que coincida con el campo anterior
            'full_name': fake_full_name,
            'date_of_birth': fake_date_of_birth,
            'phone_number': fake_phone_number,
            'address': fake_address,
            'gender': fake_gender,
            'profile_picture': fake_profile_picture,
        }

        # Crea el formulario con los datos generados aleatoriamente y pásalo a la plantilla
        form = RegistrationForm(random_data)

    return render(request, 'signup.html', {'form': form})