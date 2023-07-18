from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.register_user, name='signup'),  # Vista de registro de usuarios
    # Otras rutas para las vistas de inicio de sesión, cierre de sesión, etc., si es necesario
]
