from django.db import models
import geocoder
from django.contrib.auth import get_user_model

mapbox_token = 'pk.eyJ1IjoibGVlc2FuNjQiLCJhIjoiY2xrNzduejE0MDV0dDNnbjR0cDVtNnc4ciJ9.nA8U773QrxdRkRZiw8TlnA'


    

class Address(models.Model):
    nombre = models.TextField()
    address = models.TextField()
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.address, key=mapbox_token)
        g = g.latlng
        self.lat = g[0]
        self.long = g[1]
        return super(Address, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.address
    
CustomUser = get_user_model()

class Note(models.Model):
    OPCIONES = (
        ('Cultivo', 'Cultivo'),
        ('Terreno', 'Terreno'),
        ('Rio', 'Rio'),
    )
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=CustomUser)
    titulo = models.TextField()
    texto = models.TextField()
    nroVisita = models.AutoField(primary_key=True)
    tipo = models.CharField(
        choices=OPCIONES,
        max_length=25
    )
    fechaHora = models.DateTimeField(auto_now_add=True)
    ubic = models.ForeignKey(Address, on_delete=models.SET_NULL, blank=True, null=True)
    entrevista = models.BooleanField(default=False)
    fechaEntr = models.DateField(blank=True)
    autor = models.TextField(default='zzz')

    def __str__(self):
        return self.titulo
    

class Entrevistado(models.Model):
    nombre = models.TextField()
    apellido = models.TextField()
    edad = models.TextField()
    profesion = models.TextField()
    fechaEntr = models.DateField()

    def __str__(self):
        return self.nombre

    
    
