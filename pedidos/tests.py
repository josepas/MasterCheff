from django.test import TestCase

from django.contrib.auth.models import User
from pedidos.models import Usuario



class UsuarioTestCase(TestCase):
    def setUp(self):
      user1 = User.objects.create_user("username", "correo@gmail.com", "password")

    def test_usuario_numbers_in_name(self):
      """Usuarios """
      pass