from django.db import models

from django.forms import ModelForm

from django.contrib.auth.models import User

from django.core.validators import MinValueValidator, RegexValidator

class Billetera(models.Model):
    pin = models.CharField(max_length=4)
    saldo = models.DecimalField(max_digits=11, decimal_places=2, validators=[MinValueValidator(0)])

class Usuario(models.Model):
    TIPO = (
        ('A', 'Administrador'),
        ('C', 'Cliente'),
        ('P', 'Proveedor'),
    )
    perfil = models.OneToOneField(User) # aqui esta nombre, apellido correo y contrase;a
    cedula = models.PositiveIntegerField(null=True, blank=True,unique=True, validators=[MinValueValidator(1)]) # aqui no diferenciamos entre extranjeros y venezolanos
    rif = models.CharField(null=True, blank=True, unique=True, max_length=15, validators=[RegexValidator(regex='^J\-[0-9]+$')])
    tipo_usuario = models.CharField(max_length=1, choices=TIPO)
    fecha_nac = models.DateField(auto_now=False, auto_now_add=False)
    direccion = models.CharField(max_length=200, null=True, blank=True)
    telf = models.CharField(max_length=20, null=True, blank=True, validators=[RegexValidator(regex='^(0?[0-9]{3})([ -]?)[0-9]{3}\2?[0-9]{4}$')])
    billetera = models.OneToOneField(Billetera, null=True, blank=True)

    def __str__(self):
        return self.perfil.username

class Restaurante(models.Model):
    rif = models.CharField(max_length=15, unique=True, validators=[RegexValidator(regex='^J\-[0-9]+$')])
    admin = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    hora_apertura = models.TimeField(auto_now=False, auto_now_add=False)
    hora_cierre = models.TimeField(auto_now=False, auto_now_add=False)
    capacidad_max =  models.PositiveIntegerField(validators=[MinValueValidator(1)])

    #def __str__(self):
    #   return self.nombre


class Mesa(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    capacidad = models.PositiveIntegerField()
    ocupada = models.BooleanField(default=False)

class Sugerencias(models.Model):
    mensaje = models.CharField(max_length=30)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)


class Notificaciones(models.Model):
    mensaje = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)

class Reserva(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    mesa = models.ForeignKey(Mesa, on_delete=models.CASCADE)
    hora_ini = models.TimeField(auto_now=False, auto_now_add=False)
    hora_fin = models.TimeField(auto_now=False, auto_now_add=False)


class Producto(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    precio = models.DecimalField(max_digits=11, decimal_places=2, validators=[MinValueValidator(0)])
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    nombre = models.CharField(max_length=30)
    provedor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(validators=[MinValueValidator(0)])
    descripcion = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    precio = models.DecimalField(max_digits=11, decimal_places=2, validators=[MinValueValidator(0)])

    def __str__(self):
        return self.nombre

class Pedido(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=11, decimal_places=2, validators=[MinValueValidator(0)])

    def __str__(self):
        return "{0} total: {1}".format(self.usuario.perfil.first_name, self.total) # aqui creo que esta mal

class Factura(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    total = models.PositiveIntegerField()

class Sugerencia(models.Model):
    mensaje = models.CharField(max_length=100)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

class Menu(models.Model):
    nombre = models.CharField(max_length=30)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    productos = models.ManyToManyField(Producto)
    actual = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre



