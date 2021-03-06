from .models import Usuario, Restaurante, Producto

from django import forms
from django.forms import ModelChoiceField, ModelMultipleChoiceField, PasswordInput
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
    username = forms.CharField(
        label='Usuario', 
        max_length=100     
    )
    nombres = forms.RegexField(
        regex= r'^[a-zA-ZÁáÀàÉéÈèÍíÌìÓóÒòÚúÙùÑñüÜ ]+$',
        label='Nombres', 
        max_length=100,
        error_messages={'invalid': 'Introducir Nombres Sin Numeros'}
    )
    apellidos = forms.RegexField(
        regex= r'^[a-zA-ZÁáÀàÉéÈèÍíÌìÓóÒòÚúÙùÑñüÜ]+$',
        label='Apellidos', 
        max_length=100,
        error_messages={'invalid': 'Introducir Apellidos Sin Numeros'}
    )
    email = forms.EmailField(
        label='Correo: ejemplo@gmail.com'
    )
    direccion = forms.CharField(
        label='Direccion', 
        required=False,
        max_length=100
    )
    telefono = forms.RegexField(
        label='Teléfono: 0000-0000000', 
        regex=r'^(0?[0-9]{3})([ -]?)[0-9]{3}\2?[0-9]{4}$',
        required=False,
        max_length=100,
        error_messages={'invalid': 'Introducir formato: 0000-0000000'}
    )
    passwd = forms.CharField(
        label='Clave', 
        widget=forms.PasswordInput()
    )
    cedula = forms.IntegerField(
        min_value=1, 
        max_value=99999999,
        error_messages={'invalid': 'Cedula Invalida'}
    ) # aqui no diferenciamos entre extranjeros y venezolanos
    fecha_nac = forms.DateField(
        label='Fecha de Nacimiento: AAAA-MM-DD', 
        required=False,
        input_formats=['%Y-%m-%d'], 
        widget=forms.DateInput(), 
        validators=[fecha_futura],
        error_messages={'invalid': 'Introducir formato: AAAA-MM-DD'}
    )

class FormaRegistroProveedor(forms.Form):
    username = forms.CharField(
        label='Usuario', 
        max_length=100
    )
    nombres = forms.RegexField(
        regex= r'^[a-zA-ZÁáÀàÉéÈèÍíÌìÓóÒòÚúÙùÑñüÜ]+$',
        label='Nombres', 
        max_length=100,
        error_messages={'invalid': 'Introducir Nombres Sin Numeros'}
    )
    apellidos = forms.RegexField(
        regex= r'^[a-zA-ZÁáÀàÉéÈèÍíÌìÓóÒòÚúÙùÑñüÜ]+$',
        label='Apellidos', 
        max_length=100,
        error_messages={'invalid': 'Introducir Apellidos Sin Numeros'}
    )
    email = forms.EmailField(
        label='Correo: ejemplo@gmail.com'
    )
    direccion = forms.CharField(
        label='Direccion', 
        required=False,
        max_length=100
    )
    telefono = forms.RegexField(
        label='Teléfono: 0000-0000000', 
        regex=r'^(0?[0-9]{3})([ -]?)[0-9]{3}\2?[0-9]{4}$',
        required=False,
        max_length=100,
        error_messages={'invalid': 'Introducir formato: 0000-0000000'}
    )
    passwd = forms.CharField(
        label='Clave', 
        widget=forms.PasswordInput()
    )
    rif = forms.RegexField(
        label='Rif: J-0000000',
        regex=r'^J\-[0-9]+$', 
        min_length=8,
        max_length=10,
        error_messages={'invalid': 'Introducir formato: J-0000000'}
    )
    fecha_nac = forms.DateField(
        label='Fecha de Nacimiento: AAAA-MM-DD', 
        required=False,
        input_formats=['%Y-%m-%d'], 
        widget=forms.DateInput(), 
        validators=[fecha_futura],
        error_messages={'invalid': 'Introducir formato: AAAA-MM-DD'}
    )

class FormaRegistroRestaurante(forms.Form):
    rif = forms.RegexField(
        label='Rif: J-0000000',
        regex=r'^J\-[0-9]+$', 
        min_length=8,
        max_length=10,
        error_messages={'invalid': 'Introducir formato: J-0000000'}
    )
    nombre = forms.RegexField(
        regex= r'^[a-zA-ZÁáÀàÉéÈèÍíÌìÓóÒòÚúÙùÑñüÜ]+$',
        label='Nombre', 
        max_length=100,
        error_messages={'invalid': 'Introducir Nombres Sin Numeros'}
    )
    direccion = forms.CharField(
        max_length=30
    )
    hora_apertura = forms.TimeField(
        label='Hora Apertura: 00:00', 
        error_messages={'invalid': 'Introducir formato 00:00'})
    hora_cierre = forms.TimeField(
        label='Hora Cierre: 00:00', 
        error_messages={'invalid': 'Introducir formato 00:00'})
    capacidad_max = forms.IntegerField(
        min_value=1, 
        max_value=10000
    ) 

class RestaurantModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.nombre;
    
class ProductoModelMultipleChoiceField(ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.nombre;
    
class FormaPlato(forms.Form):
    nombre = forms.RegexField(
        regex= r'^[a-zA-ZÁáÀàÉéÈèÍíÌìÓóÒòÚúÙùÑñüÜ]+$',
        label='Nombre', 
        max_length=100,
        error_messages={'invalid': 'Introducir Nombres Sin Numeros'}
    )
    descripcion = forms.RegexField(
        regex= r'^[a-zA-ZÁáÀàÉéÈèÍíÌìÓóÒòÚúÙùÑñüÜ]+$',
        label='Ingredientes:', 
        max_length=100,
        error_messages={'invalid': 'Introducir Ingredientes Sin Numeros'}
    )
    precio = forms.DecimalField(
        label = 'Precio', 
        max_digits=11, 
        decimal_places=2
    )

class FormaCantidad(forms.Form):
    cantidad = forms.IntegerField(
        label = 'Cantidad', 
        min_value=0,
        max_value=10000, 
        error_messages={
            'min_value' : 'Ingrese una cantidad positiva',
            'invalid'   : 'Cantidad invalida'
        }
    )



class FormaBilletera(forms.Form):
    pin = forms.RegexField(
        regex= r'^\d{4}$',
        label='Pin',
        max_length= 4,
        widget=PasswordInput(),
        error_messages={'invalid': 'Pin invalido, use 4 dígitos'}
    )
    numero_tarjeta  = forms.RegexField(
        label = 'Numero Tajerta: 0000-0000-0000-0000', 
        regex= r'^[0-9]{4}[0-9]{4}[0-9]{4}[0-9]{4}$',
        max_length= 16, 
        error_messages={
            'invalid'   : 'Numero errado'
        }
    )
    saldo = forms.DecimalField(
        label = 'Saldo', 
        max_digits=11, 
        decimal_places=2,
        min_value=0,
        error_messages={
            'min_value' : 'Ingrese una cantidad positiva',
            'invalid'   : 'Cantidad invalida'
        }
    )


class AgregarServicio(forms.Form):
    nombre = forms.CharField(
        label='Nombre', 
        max_length=100     
    )

    descripcion = forms.CharField(
        label='Descripcion',
        required=False,
        min_length=1,
        max_length=200
    )

    precio = forms.DecimalField(
        label = 'Precio', 
        max_digits=9, 
        decimal_places=2,
        min_value=0,
        error_messages={
            'min_value' : 'Ingrese una cantidad positiva',
            'invalid'   : 'Cantidad invalida'
        }
    )

    cantidad = forms.IntegerField(
        label = 'Cantidad', 
        min_value=0,
        max_value=10000, 
        error_messages={
            'min_value' : 'Ingrese una cantidad positiva',
            'invalid'   : 'Cantidad invalida'
        }
    )



