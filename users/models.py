from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


# Create your models here.

class CustomUser(AbstractUser):
    ROLE = (
        ('i', 'Investigator'),
        ('v', 'Viewer'),
    )

    GENDER_CHOICES = (
        ('H', 'Hombre'),
        ('M', 'Mujer'),
        ('O', 'Otro'),
    )

    role = models.CharField(max_length=1, choices=ROLE, default='v')
    date_of_birth = models.DateField(null=True, blank=False)
    phone_number = models.CharField(max_length=20, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=False)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True,default='profile_pics/default_profile_pic.webp')

    # Nose para que es esto de abajo pero en teoria soluciona un problema de los grupos y permisos.
    #TO-DO investigar que son esas lineas.

    groups = models.ManyToManyField(Group, related_name='custom_users')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users')
