from django.test import TestCase
import unittest
from django.contrib.auth.models import User
from pedidos.models import Usuario, Billetera
from datetime import datetime
from django.core.exceptions import ValidationError

# Create your tests here.
class UsuarioTestCase(TestCase):
    def create_user(self):
        return User.objects.create(
         username = "amin123",
         email = "correo@gmail.com",
         password = "1234",
         first_name = "amin",
         last_name = "arria"
         )

    def create_billetera(self):
        return Billetera.objects.create(
            pin = "1234",
            saldo = "0"
            )

    def create_usuario(self):
        return Usuario.objects.create(
            perfil = self.create_user(),
            cedula = 24311012,
            rif = "J-241110121",
            tipo_usuario = 'A',
            fecha_nac = datetime.now(),
            direccion = "mi casa",
            telf = "0414-1112233",
            billetera = self.create_billetera()
            )

    def test_Usuario_create(self):
        u = self.create_usuario()
        u.clean_fields()
        self.assertTrue(isinstance(u,Usuario))

    def test_Usuario_cedulaCero(self):
        u = self.create_usuario()
        u.cedula = 0
        with self.assertRaises(ValidationError):
            u.clean_fields()

    def test_Usuario_cedulaNegativa(self):
        u = self.create_usuario()
        u.cedula = -123
        with self.assertRaises(ValidationError):
            u.clean_fields()

    def test_Usuario_rifFormatoIncorrecto(self):
        u = self.create_usuario()
        u.rif = "U-1234-1"
        with self.assertRaises(ValidationError):
            u.clean_fields()

    def test_Usuario_tipoIncorrecto(self):
        u = self.create_usuario()
        u.tipo_usuario = "F"
        with self.assertRaises(ValidationError):
            u.clean_fields()

    def test_Usuario_tipoIncorrecto(self):
        u = self.create_usuario()
        u.tipo_usuario = "F"
        with self.assertRaises(ValidationError):
            u.clean_fields()

    def test_Usuario_telfFormatoIncorrecto(self):
        u = self.create_usuario()
        u.telf = "12341231234"
        with self.assertRaises(ValidationError):
            u.clean_fields()