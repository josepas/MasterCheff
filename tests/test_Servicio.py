from django.test import TestCase
import unittest
from django.contrib.auth.models import User
from pedidos.models import Usuario, Billetera, Servicio
from datetime import datetime
from django.core.exceptions import ValidationError

# Create your tests here.
class ServicioTestCase(TestCase):
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
            tipo_usuario = 'P',
            fecha_nac = datetime.now(),
            direccion = "mi casa",
            telf = "0414-1112233",
            billetera = self.create_billetera()
            )

    def create_servicio(self):
        return Servicio.objects.create(
            nombre = "Mi servicio",
            provedor = self.create_usuario(),
            cantidad = 12,
            descripcion = "muy chevere",
            imagen = "foto",
            precio = 3
            )

    def test_Servicio_create(self):
        s = self.create_servicio()
        s.clean_fields()
        self.assertTrue(isinstance(s,Servicio))

    def test_Servicio_cantidadNegativa(self):
        s = self.create_servicio()
        s.cantidad = -1
        with self.assertRaises(ValidationError):
            s.clean_fields()

    def test_Servicio_precioNegativo(self):
        s = self.create_servicio()
        s.precio = -1.4
        with self.assertRaises(ValidationError):
            s.clean_fields()