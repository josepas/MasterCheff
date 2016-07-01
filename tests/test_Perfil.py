from django.test import TestCase
import unittest
from django.contrib.auth.models import User

# Create your tests here.
class PerfilTestCase(TestCase):

    def test_Perfil_create(self):
        u = User.objects.create(
         username = "amin123",
         email = "correo@gmail.com",
         password = "1234",
         first_name = "amin",
         last_name = "arria"
         )
        self.assertTrue(isinstance(u,User))