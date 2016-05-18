from django.db import models

from django.contrib.auth.models import User


class Usuario(model.Model):
	perfil = models.OneToOneField(User) # aqui esta nombre, apellido correo y contrase;a 
	cedula = models.PositiveIntegerField() # aqui no diferenciamos entre extranjeros y venezolanos
	fecha_nac = models.DateField(auto_now=False, auto_now_add=False)
	servicios = models.CharField(max_length=150) # No se como vamos a modelar esto todavia

	def __str__(self):              
        return self.perfil.name

class Restaurante(models.Model):
	rif = models.CharField(max_length=15)
	admin = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=30)
	direccion = models.CharField(max_length=30)
	hora_apertura = models.TimeField(auto_now=False, auto_now_add=False)
	hora_cierre = models.TimeField(auto_now=False, auto_now_add=False)
	capacidad_max =  models.PositiveIntegerField()

	def __str__(self):              
        return self.nombre

class Pedido(model.Model):
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	productos = models.ManyToManyField(Producto)
	restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
	total = models.DecimalField(max_digits=11, decimal_places=2) 

	def __str__(self):              
        return "{0} total: {1}".format(self.usuario, self.total) # aqui creo que esta mal


class Producto(model.Model):
	nombre = models.CharField(max_length=30)
	descripcion = models.CharField(max_length=100)
	precio = models.DecimalField(max_digits=11, decimal_places=2) 

	def __str__(self):              
        return self.nombre


class Menu(model.Model):
	nombre = models.CharField(max_length=30)
	restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
	productos = models.ManyToManyField(Producto)

	def __str__(self):              
        return self.nombre




