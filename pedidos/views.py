from .forms import FormaRegistroCliente, CrearMenuForm, FormaRegistroProveedor, FormaRegistroRestaurante, FormaPlato
from .models import Usuario, Servicio, Restaurante, Producto

from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as mch_login
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from django.core.urlresolvers import reverse


def editar_perfil(request, userID):

    mensaje = None
    print("-------------")
    print(request.user.id)
    print("-------------")

    u = User.objects.get(id=userID) 
    initial = {
        'username' : u.username,
        'nombres' : u.first_name,
        'apellidos': u.last_name,
        'cedula' : u.usuario.cedula,
        'email' : u.email,
        'rif' : u.usuario.rif
    }
    

    if request.method == 'POST':
        if u.usuario.tipo_usuario == "P":
            form = FormaRegistroProveedor()
            u.usuario.direccion=request.POST["direccion"]
            u.usuario.telf=request.POST["telefono"]
            u.usuario.save()
        elif u.usuario.tipo_usuario == "C": 
            form = FormaRegistroCliente()
            u.usuario.direccion=request.POST["direccion"]
            u.usuario.telf=request.POST["telefono"]
            u.usuario.save()
        mensaje = "Cambio exitoso"
    else:
        if u.usuario.tipo_usuario == "P":
            form = FormaRegistroProveedor(initial=initial) 
        elif u.usuario.tipo_usuario == "C":
            form = FormaRegistroCliente(initial=initial) 
        mensaje = "Ingrese nuevos Datos"      
    #     data = { 

    #     }
    # f = ContactForm(request.POST, initial=data) 
    # f.has_changed()
    return render(request, 'editar_perfil.html', {"form":form, "mensaje":mensaje})

def perfil(request):

    u = User.objects.get(username=request.user)
    # por la relacion 1 a 1 con el user model de django
    return render(request, 'perfil.html' , {'usuario': u.usuario})

def indice(request):
    return render(request, 'base.html')

def logout_view(request):
    logout(request)
    return render(request, 'base.html')

def login(request):
    mensaje = None
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            request.session['tipo'] = user.usuario.tipo_usuario
            if user.is_active:
                mch_login(request, user)
                return render(request, 'base.html')
        mensaje = 'Usuario o clave errada!'

    return render(request, 'login.html', {'mensaje':mensaje})

def registro(request):
    return render(request, 'registro.html')
    
def registroCliente(request):
    # NO logre que agarre fechas distintas a YYYY-MM-DD!

    mensaje = None
    if request.method == 'POST':

        form = FormaRegistroCliente(request.POST)
        if form.is_valid():

            try:
                u = User.objects.create_user(request.POST["username"],
                    request.POST["email"], 
                    request.POST["passwd"]
                )
            except:
                mensaje = 'Nombre de usuario en uso'
                form = FormaRegistroCliente()
                return render(request, 'registroCliente.html', {'form': form, 'mensaje':mensaje})

            u.first_name=request.POST["nombres"]
            u.last_name=request.POST["apellidos"]
            u.save()
            nuevoU = Usuario(
                perfil=u, 
                direccion=request.POST["direccion"],
                telf=request.POST["telefono"],
                cedula=request.POST["cedula"],
                fecha_nac=request.POST["fecha_nac"],
                tipo_usuario="C"
                            )
            nuevoU.save()

            mensaje = "Creado con exito!"
            form = FormaRegistroCliente()

    else:
        form = FormaRegistroCliente()

    return render(request, 'registroCliente.html', {'form': form, 'mensaje':mensaje})

def registroProveedor(request):
    # NO logre que agarre fechas distintas a YYYY-MM-DD!

    mensaje = None
    if request.method == 'POST':

        form = FormaRegistroProveedor(request.POST)
        if form.is_valid():

            try:
                u = User.objects.create_user(request.POST["username"],
                    request.POST["email"], 
                    request.POST["passwd"]
                )
            except:
                mensaje = 'Nombre de usuario en uso'
                form = FormaRegistroProveedor()
                return render(request, 'registroProveedor.html', {'form': form, 'mensaje':mensaje})

            u.first_name=request.POST["nombres"]
            u.last_name=request.POST["apellidos"]
            u.save()
            nuevoU = Usuario(
                perfil=u, 
                direccion=request.POST["direccion"],
                telf=request.POST["telefono"],
                rif=request.POST["rif"],
                fecha_nac=request.POST["fecha_nac"],
                tipo_usuario="P"
                            )
            nuevoU.save()

            mensaje = "Creado con exito!"
            form = FormaRegistroProveedor()

    else:
        form = FormaRegistroProveedor()

    return render(request, 'registroProveedor.html', {'form': form, 'mensaje':mensaje})

def agregar_servicios(request):
    proveedor = User.objects.get(username=request.user)    
    servicios = None
    if request.method == 'POST':
        print("-------------")
        print(request.POST)
        nServicio = Servicio(
            nombre = request.POST["nombre"],
            provedor = proveedor.usuario,
            descripcion = request.POST["descripcion"],
            precio = request.POST["precio"]
        )
        nServicio.save()

    servicios = proveedor.usuario.servicio_set.all()

    return render(request, 'agregar_servicios.html', {"servicios":servicios})

def eliminar_servicio(request, id):
    servicio = get_object_or_404(Servicio, pk=id).delete()
    servicios = User.objects.get(username=request.user).usuario.servicio_set.all() 

    return redirect('agregar_servicios')

def verMenu(request):
    return render(request,'verMenu.html')

def usuariosRegistrados(request):
    usuario = None
    usuarios = Usuario.objects.all()  
    return render(request,'usuariosRegistrados.html', {'usuarios':usuarios, 'usuario':usuario})

def usuarioSeleccionado(request,id):
    usuario = Usuario.objects.get(pk=id) 
    usuarios = Usuario.objects.all() 
    return render(request,'usuariosRegistrados.html', {'usuarios':usuarios, 'usuario':usuario})

def restaurantesMenu(request):
    usuario = User.objects.get(username=request.user)
    if usuario.usuario.tipo_usuario == "A":
        restaurantes = usuario.usuario.restaurante_set.all()
    elif usuario.usuario.tipo_usuario == "C":
        restaurantes = Restaurante.objects.all()
    return render(request,'restaurantesMenu.html',{'restaurantes' : restaurantes})

def restaurantesPlatos(request):
    usuario = User.objects.get(username=request.user)
    if usuario.usuario.tipo_usuario == "A":
        restaurantes = usuario.usuario.restaurante_set.all()
    elif usuario.usuario.tipo_usuario == "C":
        restaurantes = Restaurante.objects.all()
    return render(request,'restaurantesPlatos.html',{'restaurantes' : restaurantes})

def agregar_menu(request,id):
    restaurante = Restaurante.objects.get(pk=id)
    menus = restaurante.menu_set.all()
    return render(request,'agregar_menu.html', {'menus': menus, 'id':id})

def agregar_platos(request,id):
    restaurante = Restaurante.objects.get(pk=id)
    request.session['id_restaurante'] = id
    if request.method == 'POST':
        print("-------------")
        print(request.POST)
        nPlatos = Producto(
            nombre = request.POST["nombre"],
            restaurante = restaurante,
            descripcion = request.POST["descripcion"],
            precio = request.POST["precio"]
        )
        nPlatos.save()

    platos = restaurante.producto_set.all()
    return render(request,'agregar_platos.html', {'platos': platos, 'id': id})

def eliminar_plato(request, id):
    plato = get_object_or_404(Producto, pk=id).delete()
    restaurante = Restaurante.objects.get(pk=request.session['id_restaurante'])
    platos = restaurante.producto_set.all()
    return render(request,'agregar_platos.html', {'platos': platos, 'id': request.session['id_restaurante']})


def registroRestaurante(request):
    # NO logre que agarre fechas distintas a YYYY-MM-DD!

    mensaje = None
    if request.method == 'POST':
        form = FormaRegistroRestaurante(request.POST)
        if form.is_valid():
            nuevoR = Restaurante(
                rif = request.POST["rif"],
                nombre = request.POST["nombre"],
                admin = request.user.usuario,
                direccion = request.POST["direccion"],
                hora_apertura = request.POST["hora_apertura"],
                hora_cierre = request.POST["hora_cierre"],
                capacidad_max = request.POST["capacidad_max"])
            nuevoR.save()
            mensaje = "Creado con exito!"
            form = FormaRegistroRestaurante()

    else:
        form = FormaRegistroRestaurante()

    return render(request, 'registroRestaurante.html', {'form': form, 'mensaje': mensaje})

def editar_plato(request, id):
    p = Producto.objects.get(id=id) 
    initial = {
        'nombre' : p.nombre,
        'descripcion' : p.descripcion,
        'restaurante': p.restaurante,
        'precio' : p.precio,
    }
    if request.method == 'POST':
        form = FormaPlato()
        p.nombre=request.POST["nombre"]
        p.descripcion=request.POST["descripcion"]
        p.precio=request.POST["precio"]
        p.save()
        restaurante = Restaurante.objects.get(pk=request.session['id_restaurante'])
        platos = restaurante.producto_set.all()
        return render(request,'agregar_platos.html', {'platos': platos, 'id': request.session['id_restaurante']})
    else:
        form = FormaPlato(initial=initial) 
        mensaje = "Ingrese nuevos Datos"   
        return render(request, 'editar_plato.html', {"form":form})

