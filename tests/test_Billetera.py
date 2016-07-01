from django.test import TestCase
import unittest
from pedidos.models import Billetera
from django.core.exceptions import ValidationError

# Create your tests here.
class BilleteraTestCase(TestCase):
   def create_billetera(self):
      return Billetera.objects.create(
         pin = "1234",
         saldo = "0"
         )

   def test_Billetera_create(self):
      b = self.create_billetera()
      b.clean_fields()
      self.assertTrue(isinstance(b,Billetera))

   def test_Billetera_saldoNegativo(self):
      b = self.create_billetera()
      b.saldo = -0.2
      with self.assertRaises(ValidationError):
         b.clean_fields()
