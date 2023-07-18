from django.shortcuts import render, redirect
from .forms import RegistrationForm

# Create your views here.

def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirect to a success page or do something else after successful registration
            return redirect('success-page')
    else:
        form = RegistrationForm()

    return render(request, 'signup.html', {'form': form})