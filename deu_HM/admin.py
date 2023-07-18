from django.contrib import admin
from maps.models import Address
from maps.models import Note

admin.site.register(Address)
admin.site.register(Note)