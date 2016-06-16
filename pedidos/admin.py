from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Usuario, Menu, Restaurante, Billetera

admin.site.register(Usuario)
admin.site.register(Menu)
admin.site.register(Restaurante)
admin.site.register(Billetera)