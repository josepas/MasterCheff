from django.test import TestCase
import unittest
from pedidos.forms import (
    FormaRegistroCliente
)
from datetime import datetime
import sys

# Create your tests here.
class FormaRegistroTestCase(unittest.TestCase):

    def test_FormaRegistro_formaVacio(self):
        form_data = {}
        form = FormaRegistroCliente(data=form_data)
        self.assertFalse(form.is_valid())

    def test_FormaRegistro_CedulaNegativa(self):
        form_data = {
            'username': 'chris',
            'nombres': 'christopher',
            'apellidos': 'flores',
            'email' : 'christo.8.16@gmail.com',
            'direccion' : 'la candelaria',
            'telefono': '04122130917',
            'passwd' : '123',
            'cedula': -21534848,
            'fecha_nac': '1991-11-15'
        }
        form = FormaRegistroCliente(data=form_data)
        self.assertFalse(form.is_valid())