from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.register_user, name='signup'),  # Vista de registro de usuarios
    path('login/', views.user_login, name='login'),  # Vista de inicio de sesion de usuarios
    path('logout/', views.user_logout, name='logout'),  # Vista de cierre de sesion de usuarios
]
