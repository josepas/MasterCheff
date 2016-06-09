from django.test import TestCase
import unittest
from pedidos.forms import (
    FormaRegistroProveedor
)
from datetime import datetime
import sys

class FormaRegistroProveedorTestCase(unittest.TestCase):

    def test_FormaRegistroProveedor_formaVacio(self):
        form_data = {}
        form = FormaRegistroProveedor(data=form_data)
        self.assertFalse(form.is_valid())

    # # # # # # # # # # # # # # # # # # # # # # # #
    #                                             #
    #              Prueba Unitarias               #
    #                                             #
    # # # # # # # # # # # # # # # # # # # # # # # #    
    
    #Probamos los campos obligatorios, campos vacios
    def test_FormaRegistroProveedor_usernamEmpty(self):
        form_data = {
             'username' : '',
             'nombres': 'Kervyn Johan',
             'apellidos':'Rivero Mujica',
             'email':'laquemaropa@examples.com',
             'direccion':'mariperez',
             'telefono':'032232321',
             'paswd':'okwqokqwko12',
             'rif':'ker9802323232323222',
             'fecha_nac':'19-4-2004'
        }
        form = FormaRegistroProveedor(data=form_data)
        self.assertFalse(form.is_valid())

    def test_FormaRegistroProveedor_nombresEMpty(self):
        form_data={
            'username' : 'Kerivero',
            'nombres': '',
            'apellidos':'Rivero Mujica',
            'email':'laquemaropa@examples.com',
            'direccion':'mariperez',
            'telefono':'04123644886',
            'paswd':'okwqokqwko12',
            'rif':'ker9802323232323222',
            'fecha_nac':'19-4-2004'
        }
        form= FormaRegistroProveedor(data=form_data)
        self.assertFalse(form.is_valid())

    def test_FormaRegistroProveedor_apellidosEmpty(self):
        form_data={
            'username' : 'Kerivero',
            'nombres': 'Kervyn Johan',
            'apellidos':'',
            'email':'laquemaropa@examples.com',
            'direccion':'mariperez',
            'telefono':'04123644886',
            'paswd':'okwqokqwko12',
            'rif':'ker9802323232323222',
            'fecha_nac':'19-4-2004'
        }
        form= FormaRegistroProveedor(data=form_data)
        self.assertFalse(form.is_valid())

    def test_FormaRegistroProveedor_telefonoEmpty(self):       
        form_data={
            'username' : 'Kerivero',
            'nombres': 'Kervyn Johan',
            'apellidos':'Rivero Mujica',
            'email':'laquemaropa@examples.com',
            'direccion':'mariperez',
            'telefono':'',
            'paswd':'okwqokqwko12',
            'rif':'ker9802323232323222',
            'fecha_nac':'19-4-2004'
        }
        form= FormaRegistroProveedor(data=form_data)
        self.assertFalse(form.is_valid())

    def test_FormaRegistroProveedor_paswdEmpty(self):
        form_data={
            'username' : 'Kerivero',
            'nombres': 'Kervyn Johan',
            'apellidos':'Rivero Mujica',
            'email':'laquemaropa@examples.com',
            'direccion':'mariperez',
            'telefono':'04123644886',
            'paswd':'',
            'rif':'ker9802323232323222',
            'fecha_nac':'19-4-2004'
        }
        form= FormaRegistroProveedor(data=form_data)
        self.assertFalse(form.is_valid())

    def test_FormaRegistroProveedor_rifEmpty(self):
        form_data={
            'username' : 'Kerivero',
            'nombres': 'Kervyn Johan',
            'apellidos':'Rivero Mujica',
            'email':'laquemaropa@examples.com',
            'direccion':'mariperez',
            'telefono':'04123644886',
            'paswd':'okwqokqwko12',
            'rif':'',
            'fecha_nac':'19-4-2004'
        }
        form= FormaRegistroProveedor(data=form_data)
        self.assertFalse(form.is_valid())


# Probamos que los campos obligatorios mal escritos

    #DUDA CON ESTA PRUEBA
    def test_FormaRegistroProveedor_usernameWrong(self):
        form_data = {
             'username' : '',
             'nombres': 'Kervyn Johan',
             'apellidos':'Rivero Mujica',
             'email':'laquemaropa@examples.com',
             'direccion':'mariperez',
             'telefono':'032232321',
             'paswd':'okwqokqwko12',
             'rif':'ker9802323232323222',
             'fecha_nac':'19-4-2004'
        }
        form = FormaRegistroProveedor(data=form_data)
        self.assertFalse(form.is_valid())

    def test_FormaRegistroProveedor_nombresWrong(self):
        form_data={
            'username' : 'Kerivero',
            'nombres': 'Ker12vyn',
            'apellidos':'Rivero Mujica',
            'email':'laquemaropa@examples.com',
            'direccion':'mariperez',
            'telefono':'04123644886',
            'paswd':'okwqokqwko12',
            'rif':'ker9802323232323222',
            'fecha_nac':'19-4-2004'
        }
        form= FormaRegistroProveedor(data=form_data)
        self.assertFalse(form.is_valid())

    def test_FormaRegistroProveedor_apellidosWrong(self):
        form_data={
            'username' : 'Kerivero',
            'nombres': 'Kervyn Johan',
            'apellidos':'River0 MUj1c4',
            'email':'laquemaropa@examples.com',
            'direccion':'mariperez',
            'telefono':'04123644886',
            'paswd':'okwqokqwko12',
            'rif':'ker9802323232323222',
            'fecha_nac':'19-4-2004'
        }
        form= FormaRegistroProveedor(data=form_data)
        self.assertFalse(form.is_valid())

    def test_FormaRegistroProveedor_telefonoWrong(self):       
        form_data={
            'username' : 'Kerivero',
            'nombres': 'Kervyn Johan',
            'apellidos':'Rivero Mujica',
            'email':'laquemaropa@examples.com',
            'direccion':'mariperez',
            'telefono':'numeroMalo',
            'paswd':'okwqokqwko12',
            'rif':'ker9802323232323222',
            'fecha_nac':'19-4-2004'
        }
        form= FormaRegistroProveedor(data=form_data)
        self.assertFalse(form.is_valid())

    def test_FormaRegistroProveedor_paswdWrong(self):
        form_data={
            'username' : 'Kerivero',
            'nombres': 'Kervyn Johan',
            'apellidos':'Rivero Mujica',
            'email':'laquemaropa@examples.com',
            'direccion':'mariperez',
            'telefono':'04123644886',
            'paswd':'_',
            'rif':'ker9802323232323222',
            'fecha_nac':'19-4-2004'
        }
        form= FormaRegistroProveedor(data=form_data)
        self.assertFalse(form.is_valid())
#Dudas con el rif
    def test_FormaRegistroProveedor_rifWrong(self):
        form_data={
            'username' : 'Kerivero',
            'nombres': 'Kervyn Johan',
            'apellidos':'Rivero Mujica',
            'email':'laquemaropa@examples.com',
            'direccion':'mariperez',
            'telefono':'04123644886',
            'paswd':'okwqokqwko12',
            'rif':'ingenieriadeSoftware',
            'fecha_nac':'19-4-2004'
        }
        form= FormaRegistroProveedor(data=form_data)
        self.assertFalse(form.is_valid())

    #Probamos que los campos obligatorios esten bien escritos

    #DUDA CON ESTA PRUEBA
    def test_FormaRegistroProveedor_usernameGood(self):
        form_data = {
             'username' : 'kerive',
             'nombres': 'Kervyn Johan',
             'apellidos':'Rivero Mujica',
             'email':'laquemaropa@examples.com',
             'direccion':'mariperez',
             'telefono':'032232321',
             'paswd':'okwqokqwko12',
             'rif':'ker9802323232323222',
             'fecha_nac':'19-4-2004'
        }
        form = FormaRegistroProveedor(data=form_data)
        self.assertFalse(form.is_valid())

    def test_FormaRegistroProveedor_nombresGood(self):
        form_data={
            'username' : 'Kerivero',
            'nombres': 'Kervyn',
            'apellidos':'Rivero Mujica',
            'email':'laquemaropa@examples.com',
            'direccion':'mariperez',
            'telefono':'04123644886',
            'paswd':'okwqokqwko12',
            'rif':'ker9802323232323222',
            'fecha_nac':'19-4-2004'
        }
        form= FormaRegistroProveedor(data=form_data)
        self.assertFalse(form.is_valid())

    def test_FormaRegistroProveedor_apellidosGood(self):
        form_data={
            'username' : 'Kerivero',
            'nombres': 'Kervyn Johan',
            'apellidos':'Rivero Mujica',
            'email':'laquemaropa@examples.com',
            'direccion':'mariperez',
            'telefono':'04123644886',
            'paswd':'okwqokqwko12',
            'rif':'ker9802323232323222',
            'fecha_nac':'19-4-2004'
        }
        form= FormaRegistroProveedor(data=form_data)
        self.assertFalse(form.is_valid())

    def test_FormaRegistroProveedor_telefonoGood(self):       
        form_data={
            'username' : 'Kerivero',
            'nombres': 'Kervyn Johan',
            'apellidos':'Rivero Mujica',
            'email':'laquemaropa@examples.com',
            'direccion':'mariperez',
            'telefono':'04123644886',
            'paswd':'okwqokqwko12',
            'rif':'ker9802323232323222',
            'fecha_nac':'19-4-2004'
        }
        form= FormaRegistroProveedor(data=form_data)
        self.assertFalse(form.is_valid())

    def test_FormaRegistroProveedor_paswdGood(self):
        form_data={
            'username' : 'Kerivero',
            'nombres': 'Kervyn Johan',
            'apellidos':'Rivero Mujica',
            'email':'laquemaropa@examples.com',
            'direccion':'mariperez',
            'telefono':'04123644886',
            'paswd':'mipassword1234',
            'rif':'ker9802323232323222',
            'fecha_nac':'19-4-2004'
        }
        form= FormaRegistroProveedor(data=form_data)
        self.assertFalse(form.is_valid())
# #Dudas con el rif
#     def test_FormaRegistroProveedor_rifGood(self):
#         form_data={
#             'username' : 'Kerivero',
#             'nombres': 'Kervyn Johan',
#             'apellidos':'Rivero Mujica',
#             'email':'laquemaropa@examples.com',
#             'direccion':'mariperez',
#             'telefono':'04123644886',
#             'paswd':'okwqokqwko12',
#             'rif':'J123',
#             'fecha_nac':'19-4-2004'
#         }
#         form= FormaRegistroProveedor(data=form_data)
#         self.assertFalse(form.is_valid())

    # # # # # # # # # # # # # # # # # # # # # # # #
    #                                             #
    #              Prueba de Bordes               #
    #                                             #
    # # # # # # # # # # # # # # # # # # # # # # # #  
    def test_FormaRegistroProveedor_usernameEdge(self):
        form_data={
            'username' : 'Kerivero',
            'nombres': 'Kervyn Johan',
            'apellidos':'Rivero Mujica',
            'email':'laquemaropa@examples.com',
            'direccion':'mariperez',
            'telefono':'04123644886',
            'paswd':'mipassword1234',
            'rif':'ker9802323232323222',
            'fecha_nac':'19-4-2004'
        }
        form= FormaRegistroProveedor(data=form_data)
        self.assertFalse(form.is_valid())

    # # # # # # # # # # # # # # # # # # # # # # # #
    #                                             #
    #              Prueba Des Esquina             #
    #                                             #
    # # # # # # # # # # # # # # # # # # # # # # # #  

    # # # # # # # # # # # # # # # # # # # # # # # #
    #                                             #
    #              Prueba Maliciosas              #
    #                                             #
    # # # # # # # # # # # # # # # # # # # # # # # #  

    def test_FormaRegist                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  roProveedor_tlfIncorrecto(self):
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