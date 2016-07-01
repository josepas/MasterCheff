from django.test import TestCase
import unittest
from pedidos.forms import (
    FormaRegistroCliente
)
from datetime import datetime
import sys

# Create your tests here.
class FormaRegistroTestCase(TestCase):

    #Malicia
    def test_FormaRegistro_formaVacio(self):
        form_data = {}
        form = FormaRegistroCliente(data=form_data)
        self.assertFalse(form.is_valid())

    #Malicia
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

    # Malicia
    def test_FormaRegistro_TelefonoMalo(self):
        form_data = {
            'username': 'chris',
            'nombres': 'christopher',
            'apellidos': 'flores',
            'email': 'christo.8.16@gmail.com',
            'direccion': 'la candelaria',
            'telefono': 'ABSD04122130917',
            'passwd': '123',
            'cedula': 21534848,
            'fecha_nac': '1991-11-15'
        }
        form = FormaRegistroCliente(data=form_data)
        self.assertFalse(form.is_valid())

# Malicia
    def test_FormaRegistro_FechaMala(self):
        form_data = {
            'username': 'chris',
            'nombres': 'christopher',
            'apellidos': 'flores',
            'email': 'christo.8.16@gmail.com',
            'direccion': 'la candelaria',
            'telefono': '04122130917',
            'passwd': '123',
            'cedula': 21534848,
            'fecha_nac': '11-15-1991'
        }
        form = FormaRegistroCliente(data=form_data)
        self.assertFalse(form.is_valid())


#Malicia
    def test_FormaRegistro_CedulaLetra(self):
        form_data = {
            'username': 'chris',
            'nombres': 'christopher',
            'apellidos': 'flores',
            'email': 'christo.8.16@gmail.com',
            'direccion': 'la candelaria',
            'telefono': '04122130917',
            'passwd': '123',
            'cedula': 'ACV2321',
            'fecha_nac': '1991-11-15'
        }
        form = FormaRegistroCliente(data=form_data)
        self.assertFalse(form.is_valid())

#Malicia
    def test_FormaRegistro_FechaNacFutura(self):
        form_data = {
            'username': 'chris',
            'nombres': 'christopher',
            'apellidos': 'flores',
            'email': 'christo.8.16@gmail.com',
            'direccion': 'la candelaria',
            'telefono': '04122130917',
            'passwd': '123',
            'cedula': '21534848',
            'fecha_nac': '2017-11-15'
        }
        form = FormaRegistroCliente(data=form_data)
        self.assertFalse(form.is_valid())

#Malicia
    def test_FormaRegistro_NombreInvalido(self):
        form_data = {
            'username': '123',
            'nombres': 'christopher123',
            'apellidos': 'flores',
            'email': 'christo.8.16@gmail.com',
            'direccion': 'la candelaria',
            'telefono': '04122130917',
            'passwd': '123',
            'cedula': '21534848',
            'fecha_nac': '1991-11-15'
        }
        form = FormaRegistroCliente(data=form_data)
        self.assertFalse(form.is_valid())

#Malicia
    def test_FormaRegistro_NombreAcento(self):
        form_data = {
            'username': 'chris',
            'nombres': 'María',
            'apellidos': 'flores',
            'email': 'christo.8.16@gmail.com',
            'direccion': 'la candelaria',
            'telefono': '04122130917',
            'passwd': '123',
            'cedula': '21534848',
            'fecha_nac': '1991-11-15'
        }
        form = FormaRegistroCliente(data=form_data)
        self.assertTrue(form.is_valid())

#Malicia
    def test_FormaRegistro_NombreSimobolo(self):
        form_data = {
            'username': 'chris',
            'nombres': 'María!',
            'apellidos': 'flores',
            'email': 'christo.8.16@gmail.com',
            'direccion': 'la candelaria',
            'telefono': '04122130917',
            'passwd': '123',
            'cedula': '21534848',
            'fecha_nac': '1991-11-15'
        }
        form = FormaRegistroCliente(data=form_data)
        self.assertFalse(form.is_valid())

#Malicia
    def test_FormaRegistro_ApellidoInvalido(self):
        form_data = {
            'username': '123',
            'nombres': 'christopher',
            'apellidos': 'flores123',
            'email': 'christo.8.16@gmail.com',
            'direccion': 'la candelaria',
            'telefono': '04122130917',
            'passwd': '123',
            'cedula': '21534848',
            'fecha_nac': '1991-11-15'
        }
        form = FormaRegistroCliente(data=form_data)
        self.assertFalse(form.is_valid())

#Malicia
    def test_FormaRegistro_ApellidoAcento(self):
        form_data = {
            'username': 'chris',
            'nombres': 'Christopher',
            'apellidos': 'Martínez',
            'email': 'christo.8.16@gmail.com',
            'direccion': 'la candelaria',
            'telefono': '04122130917',
            'passwd': '123',
            'cedula': '21534848',
            'fecha_nac': '1991-11-15'
        }
        form = FormaRegistroCliente(data=form_data)
        self.assertTrue(form.is_valid())

#Malicia
    def test_FormaRegistro_ApellidoSimobolo(self):
        form_data = {
            'username': 'chris',
            'nombres': 'María!',
            'apellidos': 'flores',
            'email': 'christo.8.16@gmail.com',
            'direccion': 'la candelaria',
            'telefono': '04122130917',
            'passwd': '123',
            'cedula': '21534848',
            'fecha_nac': '1991-11-15'
        }
        form = FormaRegistroCliente(data=form_data)
        self.assertFalse(form.is_valid())

#Malicia
    # def test_FormaRegistro_NombreEspacio(self):
    #     form_data = {
    #         'username': 'chris',
    #         'nombres': 'María ',
    #         'apellidos': 'flores',
    #         'email': 'christo.8.16@gmail.com',
    #         'direccion': 'la candelaria',
    #         'telefono': '04122130917',
    #         'passwd': '123',
    #         'cedula': '21534848',
    #         'fecha_nac': '1991-11-15'
    #     }
    #     form = FormaRegistroCliente(data=form_data)
    #     self.assertFalse(form.is_valid())

# Malicia
    def test_FormaRegistro_ApellidoEspacio(self):
        form_data = {
            'username': 'chris',
            'nombres': 'María',
            'apellidos': 'flores ',
            'email': 'christo.8.16@gmail.com',
            'direccion': 'la candelaria',
            'telefono': '04122130917',
            'passwd': '123',
            'cedula': '21534848',
            'fecha_nac': '1991-11-15'
        }
        form = FormaRegistroCliente(data=form_data)
        self.assertFalse(form.is_valid())

#Borde
    def test_FormaRegistro_UnCampoNecesario(self):
        form_data = {
            'username': 'chris'
        }
        form = FormaRegistroCliente(data=form_data)
        self.assertFalse(form.is_valid())

#Borde
    def test_FormaRegistro_DosCampoNecesario(self):
        form_data = {
            'username': 'chris',
            'nombres': 'María',
        }
        form = FormaRegistroCliente(data=form_data)
        self.assertFalse(form.is_valid())

#Borde
    def test_FormaRegistro_TresCampoNecesario(self):
        form_data = {
            'username': 'chris',
            'nombres': 'María',
            'email': 'christo.8.16@gmail.com',

        }
        form = FormaRegistroCliente(data=form_data)
        self.assertFalse(form.is_valid())

#Borde
    def test_FormaRegistro_CuatroCampoNecesario(self):
        form_data = {
            'username': 'chris',
            'nombres': 'María',
            'email': 'christo.8.16@gmail.com',
            'passwd': '123',

        }
        form = FormaRegistroCliente(data=form_data)
        self.assertFalse(form.is_valid())

# Borde
    def test_FormaRegistro_CincoCampoNecesario(self):
        form_data = {
            'username': 'chris',
            'nombres': 'María',
            'email': 'christo.8.16@gmail.com',
            'passwd': '123',
            'cedula': '21534848',

        }
        form = FormaRegistroCliente(data=form_data)
        self.assertFalse(form.is_valid())

# Borde
    def test_FormaRegistro_SeisCampoNecesario(self):
        form_data = {
            'username': 'chris',
            'nombres': 'María',
            'apellidos': 'flores',
            'email': 'christo.8.16@gmail.com',
            'passwd': '123',
            'cedula': '21534848',

        }
        form = FormaRegistroCliente(data=form_data)
        self.assertTrue(form.is_valid())