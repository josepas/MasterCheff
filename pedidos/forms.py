from django.conf import settings    
from django import forms
from .models import Usuario


class FormaRegistro(forms.Form):
    username = forms.CharField(label='Usuario', max_length=100)
    nombres = forms.CharField(label='Nombres', max_length=100)
    apellidos = forms.CharField(label='Apellidos', max_length=100)
    passwd = forms.CharField(label='Clave', widget=forms.PasswordInput())
    cedula = forms.IntegerField(min_value=1, max_value=120000000) # aqui no diferenciamos entre extranjeros y venezolanos
    fecha_nac = forms.DateField(label='Fecha de Nacimiento', input_formats=['%Y-%m-%d'], widget=forms.DateInput() )




class FormaRestaurante(forms.Form):
    rif = forms.CharField(label='Rif', max_length=15)
    nombre = forms.CharField(label='Nombre', max_length=30)
    admin = forms.ModelChoiceField(queryset=Usuario.objects.all())
    direccion = forms.CharField(max_length=30)
    hora_apertura = forms.TimeField()
    hora_cierre = forms.TimeField()
    capacidad_max = forms.IntegerField(min_value=1, max_value=10000) 
