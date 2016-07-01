from django.test import TestCase
import unittest
from django.contrib.auth.models import User
from pedidos.models import Usuario, Billetera, Restaurante, Producto
from datetime import datetime
from django.core.exceptions import ValidationError

# Create your tests here.
class ProductoTestCase(TestCase):
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

    def create_producto(self):
        return Producto.objects.create(
            nombre = "Mi Producto",
            descripcion = "Muy fino",
            imagen = "blad",
            precio = 12,
            restaurante = self.create_restaurante()
            )

    def test_Producto_create(self):
        p = self.create_producto()
        p.clean_fields()
        self.assertTrue(isinstance(p,Producto))

    def test_Producto_precioNegativo(self):
        p = self.create_producto()
        p.precio = -1
        with self.assertRaises(ValidationError):
            p.clean_fields()