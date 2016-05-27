from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Usuario, Menu, Restaurante

admin.site.register(Usuario)
admin.site.register(Menu)
admin.site.register(Restaurante)