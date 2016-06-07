from django.test import TestCase
from pedidos.forms import FormaRegistroRestaurante
from datetime import time

class FormaRegistroRestauranteTestCase(TestCase):
    def setUp(self):
        self.form_data = {
                'rif' :"j-1234",
                "nombre" : "Mi Restaurante",
                "direccion" : "Calle esta, Urb Otra",
                "hora_apertura" : time(8),
                "hora_cierre" : time(17),
                "capacidad_max" : 22
            }

    def test_form_vacio(self):
        form_data = {}
        form = FormaRegistroRestaurante(data=form_data)
        self.assertFalse(form.is_valid())

    def test_capacidad_negativa(self):
        form_data = self.form_data
        form_data["capacidad_max"] = -1
        form = FormaRegistroRestaurante(data=form_data)
        self.assertFalse(form.is_valid())

    # def test_nombre_con_numero(self):
    #     form_data = self.form_data
    #     form_data["nombre"] = "nombre123"
    #     form = FormaRegistroRestaurante(data=form_data)
    #     self.assertFalse(form.is_valid())

    # def test_hora_apertura_menor_cierre(self):
    #     form_data = self.form_data
    #     form_data["hora_apertura"] = time(17)
    #     form_data["hora_cierre"] = time(8)
    #     form = FormaRegistroRestaurante(data=form_data)
    #     self.assertFalse(form.is_valid())
