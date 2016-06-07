from .models import Usuario, Restaurante, Producto

from django import forms
from django.forms import ModelChoiceField, ModelMultipleChoiceField
from django.forms.widgets import SplitDateTimeWidget

from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

from decimal import *
from datetime import date

def fecha_futura(fecha):
    if fecha > date.today():
        raise ValidationError('Fecha invalida, valor futuro')

def validate_telefono(value):
    regex = r'^((0?[0-9]{3})([ -]?)[0-9]{3}\2?[0-9]{4})$'
    if not re.match(regex, value):
        raise ValidationError('telefono_invalido')

class FormaRegistroCliente(forms.Form):
    username = forms.CharField(label='Usuario', max_length=100)
    nombres = forms.CharField(label='Nombres', max_length=100)
    apellidos = forms.CharField(label='Apellidos', max_length=100)
    email = forms.EmailField(label='Correo')
    direccion = forms.CharField(
        label='Direccion', 
        required=False,
        max_length=100
    )
    telefono = forms.RegexField(label='Teléfono', 

        regex=r'^(0?[0-9]{3})([ -]?)[0-9]{3}\2?[0-9]{4}$',
        required=False,
        max_length=100,
        error_messages={'invalid': 'Formato de teléfono inválido'}
    )

    passwd = forms.CharField(label='Clave', widget=forms.PasswordInput())
    cedula = forms.IntegerField(min_value=1, max_value=120000000) # aqui no diferenciamos entre extranjeros y venezolanos
    fecha_nac = forms.DateField(label='Fecha de Nacimiento', 
        required=False,
        input_formats=['%Y-%m-%d'], 
        widget=forms.DateInput(), 
        validators=[fecha_futura],
        error_messages={'invalid': 'Formato inválido AAAA-MM-DD'}
    )

class FormaRegistroProveedor(forms.Form):
    username = forms.CharField(label='Usuario', max_length=100)
    nombres = forms.CharField(label='Nombres', max_length=100)
    apellidos = forms.CharField(label='Apellidos', max_length=100)
    email = forms.EmailField(label='Correo')
    direccion = forms.CharField(
        label='Direccion', 
        required=False,
        max_length=100
    )
    telefono = forms.RegexField(label='Teléfono', 

        regex=r'^(0?[0-9]{3})([ -]?)[0-9]{3}\2?[0-9]{4}$',
        required=False,
        max_length=100,
        error_messages={'invalid': 'Formato de teléfono inválido'}
    )

    passwd = forms.CharField(label='Clave', widget=forms.PasswordInput())
    rif = forms.CharField(label='Rif', max_length=15)
    fecha_nac = forms.DateField(label='Fecha de Nacimiento', 
        required=False,
        input_formats=['%Y-%m-%d'], 
        widget=forms.DateInput(), 
        validators=[fecha_futura],
        error_messages={'invalid': 'Formato inválido AAAA-MM-DD'}
    )

class FormaRegistroRestaurante(forms.Form):
    rif = forms.CharField(label='Rif', max_length=15)
    nombre = forms.CharField(label='Nombre', max_length=30)
    direccion = forms.CharField(max_length=30)
    hora_apertura = forms.TimeField()
    hora_cierre = forms.TimeField()
    capacidad_max = forms.IntegerField(min_value=1, max_value=10000) 


class RestaurantModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.nombre;
    
class ProductoModelMultipleChoiceField(ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.nombre;

class CrearMenuForm(forms.Form):
    nombre = forms.CharField(
        required = True,
        label = 'Nombre del Menu',
        widget = forms.TextInput(attrs =
            { 'class'       : 'form-control'
            , 'placeholder' : 'ID'
            }
        )
    )
    
    restaurante = RestaurantModelChoiceField(
        queryset      = Restaurante.objects.all(),
        empty_label   = "Restaurante",
        required      = True,
        label         = 'Restaurante',
        widget        = forms.Select(
            attrs =
            { 'class' : 'form-control' }
        )
    )
    
    productos = ProductoModelMultipleChoiceField(
        queryset      = Producto.objects.all(),
        required      = False,
        label         = 'Platos'
    )

