from django.db import models
import geocoder

mapbox_token = 'pk.eyJ1IjoibGVlc2FuNjQiLCJhIjoiY2xrNzduejE0MDV0dDNnbjR0cDVtNnc4ciJ9.nA8U773QrxdRkRZiw8TlnA'

class Address(models.Model):
    address = models.TextField()
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    notas = models.ManyToManyField

    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.address, key=mapbox_token)
        g = g.latlng
        self.lat = g[0]
        self.long = g[1]
        return super(Address, self).save(*args, **kwargs)
    
    def __str__(self):
         return self.address
    

class Note(models.Model):
    titulo = models.TextField()
    texto = models.TextField()
    ubic = models.ForeignKey(Address, on_delete=models.CASCADE)
    hora = models.TimeField()

    def __str__(self):
         return self.titulo
