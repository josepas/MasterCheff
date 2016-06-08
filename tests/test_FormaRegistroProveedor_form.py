from django.test import TestCase
import unittest
from pedidos.forms import (
    FormaRegistroProveedor
)
from datetime import datetime
import sys

# Create your tests here.
class FormaRegistroProveedorTestCase(unittest.TestCase):

    def test_FormaRegistroProveedor_formaVacio(self):
        form_data = {}
        form = FormaRegistroProveedor(data=form_data)
        self.assertFalse(form.is_valid())
    
    # def test_FormaRegistroProveedor_rifIncorrecto(self):
    #     form_data={
    #         'username' : 'Kerivero',
    #         'nombres': 'Kervyn Johan',
    #         'apellidos':'Rivero Mujica',
    #         'email':'laquemaropa@examples.com',
    #         'direccion':'mariperez',
    #         'telefono':'032232321',
    #         'paswd':'okwqokqwko12',
    #         'rif':'ker9802323232323222',
    #         'fecha_nac':'19-4-2004'
    #     }
    #     form= FormaRegistroProveedor(data=form_data)
    #     self.assertFalse(form.is_valid())
# malicia
    def test_FormaRegistroProveedor_tlfIncorrecto(self):
        form_data={
            'username' : 'Kerivero',
            'nombres': 'Kervyn Johan',
            'apellidos':'Rivero Mujica',
            'email':'laquemaropa@examples.com',
            'direccion':'mariperez',
            'telefono':'03223230ker0',
            'paswd':'okwqokqwko12',
            'rif':'J12122112213',
            'fecha_nac':'19-4-2004'
        }
        form= FormaRegistroProveedor(data=form_data)
        self.assertFalse(form.is_valid())

    def test_FormaRegistroProveedor_fechaIncorrecta(self):
        form_data={
            'username' : 'Kerivero',
            'nombres': 'Kervyn Johan',
            'apellidos':'Rivero Mujica',
            'email':'laquemaropa@examples.com',
            'direccion':'mariperez',
            'telefono':'03223230',
            'paswd':'okwqokqwko12',
            'rif':'J12122112213',
            'fecha_nac':'19-4-2020'
        }
        form= FormaRegistroProveedor(data=form_data)
        self.assertFalse(form.is_valid())