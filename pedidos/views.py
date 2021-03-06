from .forms import *
from .models import Usuario, Servicio, Restaurante, Producto, Menu, Billetera, Pedido, Notificaciones, Factura, PedidoServicio, Sugerencias

from django.shortcuts import get_object_or_404, get_list_or_404
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

def listar_proveedores(request):
    proveedores = get_list_or_404(Usuario, tipo_usuario='P')  

    

    return render(request, 'listar_proveedores.html', {"proveedores" : proveedores})

def listar_servicios(request,id):
    servicios = get_list_or_404(Servicio, provedor_id=id)

    pedido = PedidoServicio.objects.last()

    if pedido is None:
        pedido = PedidoServicio(
            usuario = get_object_or_404(Usuario, pk=id),
            total = 0
        )
        pedido.save()
        
    return render(request, 'listar_servicios.html', {"servicios" : servicios, "pedidos" : pedido.servicios.all(), "pedido" : pedido})

def comprar_servicio(request, id):
    servicio = get_object_or_404(Servicio, pk=id)
    mensaje = None
    if request.method == 'POST':
        form = FormaCantidad(request.POST)
        
        if form.is_valid():

            if form.cleaned_data["cantidad"] < servicio.cantidad:
                cant = form.cleaned_data["cantidad"]

                try:
                    pedido = PedidoServicio.objects.last()

                except Pedido.DoesNotExist:
                    pedido = Pedido(
                        usuario = request.user.usuario,
                        restaurante = restaurante,
                        total = 0
                    )
                    pedido.save()
                pedido.total += servicio.precio * cant
                pedido.save()
                pedido.servicios.add(servicio)
                print(pedido.id)
                servicio.cantidad -= cant
                servicio.save()

                return redirect('listar_servicios', id=servicio.provedor.id)

            else:
                mensaje = "Cantidad Invalida"
    
    else:
        form = FormaCantidad()
    
    return render(request, 'comprar_servicio.html', {"form": form, "servicio" : servicio, "mensaje":mensaje})


def agregar_servicios(request):
    proveedor = User.objects.get(username=request.user)    
    servicios = None
    form = AgregarServicio()
    if request.method == 'POST':
        form = AgregarServicio(request.POST)
        if form.is_valid():

            nServicio = Servicio(
                nombre = form.cleaned_data["nombre"],
                provedor = proveedor.usuario,
                descripcion = form.cleaned_data["descripcion"],
                precio = form.cleaned_data["precio"],
                cantidad = form.cleaned_data["cantidad"]
            )
            nServicio.save()

    servicios = proveedor.usuario.servicio_set.all()

    return render(request, 'agregar_servicios.html', {"servicios":servicios, "form":form})

def modificar_servicio(request, id):
    servicio = get_object_or_404(Servicio, pk=id)
    data = { 
        "nombre" : servicio.nombre,
        "descripcion" : servicio.descripcion,
        "precio" : servicio.precio,
        "cantidad" : servicio.cantidad
    }

    if request.method == 'POST':
        form = AgregarServicio(request.POST, initial=data)

        if form.has_changed():

            if form.is_valid():
                servicio.nombre = form.cleaned_data["nombre"]
                servicio.descripcion = form.cleaned_data["descripcion"]
                servicio.precio = form.cleaned_data["precio"]
                servicio.cantidad = form.cleaned_data["cantidad"]
                servicio.save()

        return redirect('agregar_servicios')

    else:
        
        form = AgregarServicio(data)

    return render(request, 'modificar_servicios.html', {"form":form, "servicio":id})

def pagar_servicios(request, id):
    
    pedido = get_object_or_404(PedidoServicio, pk=id)
    proveedorID = pedido.usuario.id


    f = Factura(
        usuario = pedido.usuario,
        restaurante = None,
        total = pedido.total
    )
    f.save()

    pedido.delete()

    return redirect(listar_servicios, id=proveedorID)


def eliminar_servicio(request, id):
    servicio = get_object_or_404(Servicio, pk=id).delete()

    return redirect('agregar_servicios')

def listasMenu(request, id, idmenu):
    restaurante = Restaurante.objects.get(pk=id)
    request.session['id_restaurante'] = id
    menus = restaurante.menu_set.all()

    if int(idmenu) != 0:
        menuvisible = Menu.objects.get(pk=idmenu)
        platos = menuvisible.productos.all()
    else:
        menuvisible = None
        platos = None

    return render(request,'listasMenu.html', {'menus':menus, 'restaurante':restaurante, 'idmenu' : int(idmenu), 'menuvisible' : menuvisible, 'platos' : platos})

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

def agregar_platos(request,id):
    restaurante = Restaurante.objects.get(pk=id)
    request.session['id_restaurante'] = id
    if request.method == 'POST':
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

def eliminar_plato_menu(request, id, idmenu, idplato):
    producto = Producto.objects.get(pk=idplato)
    menu = Menu.objects.get(pk=idmenu)   
    menu.productos.remove(producto)
    return redirect('listasMenu', id=id, idmenu=idmenu)

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

def agregar_menu(request,id):
    restaurante = Restaurante.objects.get(pk=id)
    request.session['id_restaurante'] = id
    if request.method == 'POST':
        ListaDeProductos=request.POST.getlist('checks[]')
        nMenu = Menu(
            nombre = request.POST["nombre"],
            restaurante = restaurante,
        )
        nMenu.save()
        for productoID in ListaDeProductos:
            producto = Producto.objects.get(id=productoID)
            nMenu.productos.add(producto)

        #if dic[id] == None:
        #    dic[id] = nMenu.id
        '''
        usuario = User.objects.get(username=request.user)
        if usuario.usuario.tipo_usuario == "A":
            restaurantes = usuario.usuario.restaurante_set.all()
        elif usuario.usuario.tipo_usuario == "C":
            restaurantes = Restaurante.objects.all()
        return render(request,'restaurantesMenu.html',{'restaurantes' : restaurantes})
        '''
        restaurante = Restaurante.objects.get(pk=request.session['id_restaurante'])
        menus = restaurante.menu_set.all()
        return redirect('listasMenu', id=id, idmenu=nMenu.id)

    platos = restaurante.producto_set.all()
    return render(request,'agregar_menu.html', {'platos':platos,'id':id, 'restaurante' : restaurante})

def editar_menu(request, id, idmenu):
    m = Menu.objects.get(id=id) 
    initial = {
        'nombre' : m.nombre,
        'productos' : m.productos,
    }
    '''
    if request.method == 'POST':
        p.nombre=request.POST["nombre"]
        p.descripcion=request.POST["descripcion"]
        p.precio=request.POST["precio"]
        p.save()
        restaurante = Restaurante.objects.get(pk=request.session['id_restaurante'])
        platos = restaurante.producto_set.all()
        return render(request,'agregar_platos.html', {'platos': platos, 'id': request.session['id_restaurante']})
    else:

    form = FormaPlato(initial=initial) 
    '''
    mensaje = "Ingrese nuevos Datos"   
    return render(request, 'editar_menu.html', { "nombre" :  m.nombre, "productos" : m.productos })

def eliminar_menu(request, id):
    menu = get_object_or_404(Menu, pk=id).delete()
    restaurante = Restaurante.objects.get(pk=request.session['id_restaurante'])
    menus = restaurante.menu_set.all()
    return redirect('listasMenu', id=restaurante.id, idmenu=0)

def mostrar_menu_actual(request,id):
    restaurante = Restaurante.objects.get(pk=id)
    request.session['id_restaurante'] = id
    menus = restaurante.menu_set.all()
    idRestaurante = request.session['id_restaurante'] 
    for menu in menus:
        if menu.actual == True:
            menu_actual = menu.productos.all()
            return render(request, 'mostrarMenu.html', {"menu_actual":menu_actual, "id":idRestaurante})

def mostrar_menu(request,id):
    menu = Menu.objects.get(pk=id)
    request.session['id_menu'] = id    
    menu_actual = menu.productos.all()
    return render(request, 'mostrarMenu.html', {"menu_actual":menu_actual})

def seleccionar_menu_actual(request,id):
    restaurante = Restaurante.objects.get(pk=request.session['id_restaurante'])
    menus = restaurante.menu_set.all()
    for menu in menus:
        menu.actual = False
        if (int(menu.id)) == (int(id)):
            menu.actual = True
        menu.save()
    usuario = User.objects.get(username=request.user)
    if usuario.usuario.tipo_usuario == "A":
        restaurantes = usuario.usuario.restaurante_set.all()
    elif usuario.usuario.tipo_usuario == "C":
        restaurantes = Restaurante.objects.all()
    return render(request,'restaurantesMenu.html',{'restaurantes' : restaurantes})

def agregar_menu_platos(request, id, idmenu):
    restaurante = Restaurante.objects.get(pk=request.session['id_restaurante'])
    menu = Menu.objects.get(pk=idmenu)

    if request.method == 'POST':
        ListaDeProductos=request.POST.getlist('checks[]')
        for productoID in ListaDeProductos:
            producto = Producto.objects.get(id=productoID)
            menu.productos.add(producto)

        #if dic[id] == None:
        #    dic[id] = nMenu.id
        '''
        usuario = User.objects.get(username=request.user)
        if usuario.usuario.tipo_usuario == "A":
            restaurantes = usuario.usuario.restaurante_set.all()
        elif usuario.usuario.tipo_usuario == "C":
            restaurantes = Restaurante.objects.all()
        return render(request,'restaurantesMenu.html',{'restaurantes' : restaurantes})
        '''
        menus = restaurante.menu_set.all()
        return redirect('listasMenu', id=id, idmenu=idmenu)

    platos = restaurante.producto_set.all()
    return render(request,'agregar_menu_platos.html', {'platos':platos,'id':id, 'menu' : menu})

def gestionar_billetera(request, userID):
    u = User.objects.get(username=request.user)
    mensaje = None
    if request.method == 'POST':
        form = FormaBilletera(request.POST)
        if form.is_valid():
            
            # Si el usuario posee billetera creada
            if u.usuario.billetera:
                # Clave correcta
                if u.usuario.billetera.pin == request.POST["pin"]:
                    u.usuario.billetera.saldo += form.cleaned_data["saldo"]
                    mensaje = "Saldo cargado exitosamente"
                    u.usuario.billetera.save()
                else:
                    mensaje = "Pin incorrecto"
                
                form = FormaBilletera()
            else:
                b1 = Billetera(
                    pin= request.POST["pin"],
                    saldo= form.cleaned_data["saldo"]
                )    
                b1.save()

                u.usuario.billetera = b1
                u.usuario.save()

    else:
        form = FormaBilletera()
        
    return render(request, 'gestionar_billetera.html', {'form':form, 'mensaje':mensaje})

def agregar_plato_pedido(request,idPlato):

    restaurante = Restaurante.objects.get(pk=request.session['id_restaurante'])
    menus = restaurante.menu_set.all()
    plato = Producto.objects.get(pk=idPlato)

    try:
        pedido = Pedido.objects.get(usuario=request.user.usuario, restaurante=restaurante)
    except Pedido.DoesNotExist:
        pedido = Pedido(
            usuario = request.user.usuario,
            restaurante = restaurante,
            total = 0
        )
        pedido.save()

    pedido.total += plato.precio
    pedido.save()
    pedido.productos.add(plato)
    idRestaurante = request.session['id_restaurante'] 

    for menu in menus:
        if menu.actual == True:
            menu_actual = menu.productos.all()
            return render(request, 'mostrarMenu.html', {"menu_actual":menu_actual,"id":idRestaurante})

def mostrar_pedidos(request,idRestaurante):
    mensaje = None
    restaurante = Restaurante.objects.get(pk=idRestaurante)
    request.session['id_restaurante'] = idRestaurante
    try:
        pedido = Pedido.objects.get(usuario=request.user.usuario, restaurante=restaurante)
    except Pedido.DoesNotExist:
        pedido = Pedido(
            usuario = request.user.usuario,
            restaurante = restaurante,
            total = 0
        )
        pedido.save()
    pedido_usuario = pedido.productos.all()
    return render(request, 'mostrarPedido.html', {"pedido_usuario":pedido_usuario, "total":pedido.total, "mensaje":mensaje, "idRest":request.session['id_restaurante'] })

def pagar_pedido(request):
    restaurante = Restaurante.objects.get(pk=request.session['id_restaurante'])
    pedido = Pedido.objects.get(usuario=request.user.usuario, restaurante=restaurante)
    pedido_usuario = pedido.productos.all()

    billetera = request.user.usuario.billetera

    if billetera.saldo < pedido.total:
        mensaje = "Saldo insuficiente para pagar la orden"
        return render(request, 'mostrarPedido.html', {"pedido_usuario":pedido_usuario, "total":pedido.total, "mensaje":mensaje, "idRest":request.session['id_restaurante'] })

    else:
        billetera.saldo -= pedido.total
        billetera.save()
        administrador = Usuario.objects.get(tipo_usuario='A')
        administrador.billetera.saldo += pedido.total
        administrador.billetera.save()
        pedido.delete()
        factura = Factura(
            usuario = request.user.usuario,
            restaurante = restaurante,
            total = pedido.total,
        )
        factura.save()
    return render(request, 'base.html')

def cancelar_pedido(request):
    restaurante = Restaurante.objects.get(pk=request.session['id_restaurante'])
    pedido = Pedido.objects.get(usuario=request.user.usuario, restaurante=restaurante).delete()
    return render(request, 'base.html')

def agregar_notificacion(request):
    if request.method == 'POST':
        nNotificacion = Notificaciones(
            mensaje = request.POST["mensaje"],
        )
        nNotificacion.save()
    notificaciones = Notificaciones.objects.all()
    return render(request,'notificaciones.html', {'notificaciones': notificaciones})

def eliminar_notificacion(request, id):
    notificacion = get_object_or_404(Notificaciones, pk=id).delete()
    notificaciones = Notificaciones.objects.all()
    return render(request,'notificaciones.html', {'notificaciones': notificaciones})

def egresos_ingresos(request):
    facturas = Factura.objects.all().order_by('usuario')
    print(facturas)
    return render(request,'egresos_ingresos.html', {'facturas':facturas})

def agregar_sugerencia(request): 
    u = User.objects.get(username=request.user) 
    if request.method == 'POST':
        nSugerencia = Sugerencias(
            mensaje = request.POST["mensaje"],
            usuario = u.usuario
        )
        nSugerencia.save()
    sugerencias = Sugerencias.objects.filter(usuario=u.usuario.id)
    return render(request,'sugerencias.html', {'sugerencias': sugerencias})

def eliminar_sugerencia(request, id):
    u = User.objects.get(username=request.user) 
    sugerencia = get_object_or_404(Sugerencias, pk=id).delete()
    sugerencias = Sugerencias.objects.filter(usuario=u.usuario.id)
    return render(request,'sugerencias.html', {'sugerencias': sugerencias})

def mostrar_sugerencias(request):
    sugerencias = Sugerencias.objects.all()
    return render(request,'sugerencias.html', {'sugerencias': sugerencias})
