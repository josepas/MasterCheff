from django.test import TestCase
import unittest
from pedidos.forms import (
    FormaBilletera
)

# Create your tests here.
class FormaBilleteraTestCase(TestCase):

    # malicia
    def test_FormaBilletera_vacio(self):
        form_data = {}
        form = FormaBilletera(data=form_data)
        self.assertFalse(form.is_valid())

    #Borde
    def test_FormaBilletera_unCampo(self):
        form_data = {
            'pin': '1234',
            'saldo': None
        }
        form = FormaBilletera(data=form_data)
        self.assertFalse(form.is_valid())

    #Borde
    def test_FormaBilletera_DosCampos(self):
        form_data = {
            'pin': '1234',
            'saldo': 100
        }
        form = FormaBilletera(data=form_data)
        self.assertTrue(form.is_valid())

    #Malicia
    def test_FormaBilletera_PinInvalido(self):
        form_data = {
            'pin': 'ACVC',
            'saldo': 100
        }
        form = FormaBilletera(data=form_data)
        self.assertFalse(form.is_valid())

    # Malicia
    def test_FormaBilletera_SaldoInvalido(self):
        form_data = {
            'pin': '1234',
            'saldo': 'ACBSA'
        }
        form = FormaBilletera(data=form_data)
        self.assertFalse(form.is_valid())