from django.db import models
import geocoder
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core import validators

mapbox_token = 'pk.eyJ1IjoibGVlc2FuNjQiLCJhIjoiY2xrNzduejE0MDV0dDNnbjR0cDVtNnc4ciJ9.nA8U773QrxdRkRZiw8TlnA'



class Address(models.Model):
    OPCIONES = (
        ('Cultivo', 'Cultivo'),
        ('Terreno', 'Terreno'),
        ('Rio', 'Rio'),
    )
    tipo = models.CharField(
        choices=OPCIONES,
        max_length=25,
        null=True
    )
    nombre = models.TextField()
    address = models.TextField()
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    
    def __str__(self):
        return self.address

CustomUser = get_user_model()
class Note(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=CustomUser)
    titulo = models.TextField()
    texto = models.TextField()
    nroVisita = models.AutoField(primary_key=True)
    fechaHora = models.DateTimeField(auto_now_add=True)
    ubic = models.ForeignKey(Address, on_delete=models.CASCADE)
    entrevista = models.BooleanField(default=True)
    fechaEntr = models.DateField(null=True, blank=True)
    imagen = models.ImageField(upload_to='fotos/', blank=True, null=True)

    def __str__(self):
        return self.titulo
    


    
class Entrevistado(models.Model):
    nombre = models.TextField()
    apellido = models.TextField()
    edad = models.TextField(validators=[validators.RegexValidator(r'^[0-9]+$', 'Ingrese un valor numérico válido.')])
    profesion = models.TextField()
    nota = models.ForeignKey('Note', on_delete=models.CASCADE, related_name='entrevistados', blank=True, null=True)

    def __str__(self):
        return self.nombre
    
