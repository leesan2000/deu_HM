from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.widgets import PasswordInput
from .models import CustomUser
from bootstrap_datepicker_plus.widgets import DatePickerInput

class PasswordStyleMixin:
    def set_password_input_style(self):
        # Check if the form has 'password1' and 'password2' fields (RegistrationForm)
        if 'password1' in self.fields and 'password2' in self.fields:
            self.fields['password1'].widget = PasswordInput(attrs={'placeholder': 'Contraseña', 'class': 'form-control'})
            self.fields['password2'].widget = PasswordInput(attrs={'placeholder': 'Confirmar contraseña', 'class': 'form-control'})
        # Check if the form has 'password' field (AuthenticationForm)
        elif 'password' in self.fields:
            self.fields['password'].widget = PasswordInput(attrs={'placeholder': 'Contraseña', 'class': 'form-control'})

class RegistrationForm(PasswordStyleMixin, UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'date_of_birth', 'phone_number', 'gender', 'profile_picture')
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Nombre', 'class': 'form-control', 'required': 'required'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Apellido', 'class': 'form-control'}),
            'username': forms.TextInput(attrs={'placeholder': 'Nombre de usuario', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Correo electrónico', 'class': 'form-control'}),
            'date_of_birth': DatePickerInput(
                options={
                    "format": "DD/MM/YYYY", # moment date-time format
                    "showClose": True,
                    "showClear": True,
                    "showTodayButton": True,
                    "locale": "es",
                },
                attrs={'class': 'form-control'}
            ),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Número de teléfono', 'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'profile_picture': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_password_input_style()

class CustomLoginForm(forms.Form):
    usernameLogin = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario', 'class': 'form-control'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'class': 'form-control'})
    )
    remember_me = forms.BooleanField(required=False, initial=True)

    def set_password_input_style(self):
        if 'password' in self.fields:
            self.fields['password'].widget = PasswordInput(attrs={'placeholder': 'Contraseña', 'class': 'form-control'})

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_password_input_style()