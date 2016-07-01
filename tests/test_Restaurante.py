from django.test import TestCase
import unittest
from django.contrib.auth.models import User
from pedidos.models import Usuario, Billetera, Restaurante
from datetime import datetime
from django.core.exceptions import ValidationError

# Create your tests here.
class RestauranteTestCase(TestCase):
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

    def create_restaurante(self):
        return Restaurante.objects.create(
            rif = "J-24311022",
            admin = self.create_usuario(),
            nombre = "Mi Restaurante",
            direccion = "En ese lugar",
            hora_apertura = datetime.now(),
            hora_cierre = datetime.now(),
            capacidad_max = 34
            )

    def test_Restaurante_create(self):
        r = self.create_restaurante()
        r.clean_fields()
        self.assertTrue(isinstance(r,Restaurante))

    def test_Restaurante_rifFormatoIncorrecto(self):
        r = self.create_restaurante()
        r.rif = "U-1234-1"
        with self.assertRaises(ValidationError):
            r.clean_fields()

    def test_Restaurante_capacidadCero(self):
        r = self.create_restaurante()
        r.capacidad_max = 0
        with self.assertRaises(ValidationError):
            r.clean_fields()

    def test_Restaurante_capacidadNegativa(self):
        r = self.create_restaurante()
        r.capacidad_max = -2
        with self.assertRaises(ValidationError):
            r.clean_fields()