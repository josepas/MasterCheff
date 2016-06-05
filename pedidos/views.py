from .forms import FormaRegistro, FormaRestaurante, CrearMenuForm
from .models import Usuario


from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as mch_login
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from django.core.urlresolvers import reverse


def editar_perfil(request, userID):

    mensaje = None
    u = User.objects.get(id=userID) 
    initial = {
        'username' : u.username,
        'nombres' : u.first_name,
        'apellidos': u.last_name,
        'cedula' : u.usuario.cedula,
        'email' : u.email
    }
    

    if request.method == 'POST':
        form = FormaRegistro()
        u.usuario.direccion=request.POST["direccion"]
        u.usuario.telf=request.POST["telefono"]
        u.usuario.save()
        mensaje = "Cambio exitoso"

    else:
        form = FormaRegistro(initial=initial) 
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
    return redirect('indice')

def login(request):

    mensaje = None
    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                mch_login(request, user)
                return redirect('indice')

        mensaje = 'Usuario o clave errada!'

    return render(request, 'login.html', {'mensaje':mensaje})


def registro(request):
    # NO logre que agarre fechas distintas a YYYY-MM-DD!

    mensaje = None
    if request.method == 'POST':

        form = FormaRegistro(request.POST)
        if form.is_valid():

            try:
                u = User.objects.create_user(request.POST["username"],
                    request.POST["email"], 
                    request.POST["passwd"]
                )
            except:
                mensaje = 'Nombre de usuario en uso'
                form = FormaRegistro()
                return render(request, 'registro.html', {'form': form, 'mensaje':mensaje})

            u.first_name=request.POST["nombres"]
            u.last_name=request.POST["apellidos"]
            u.save()
            nuevoU = Usuario(
                perfil=u, 
                direccion=request.POST["direccion"],
                telf=request.POST["telefono"],
                cedula=request.POST["cedula"],
                fecha_nac=request.POST["fecha_nac"]
            )
            nuevoU.save()

            mensaje = "Creado con exito!"
            form = FormaRegistro()

    else:
        form = FormaRegistro()

    return render(request, 'registro.html', {'form': form, 'mensaje':mensaje})


def agregar_servicios(request):
    
    return render(resquest, 'agregar_servicios.html')





def registroRestaurante(request):
    if request.method == 'POST':
        form = FormaRestaurante(request.POST)
        if form.is_valid():
            pass

    else:
        form = FormaRestaurante() 

    return render(request, 'registroRestaurante.html', {'form': form})

def menu_crear(request):

    if request.method == 'POST':
        form = CrearMenuForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = CrearMenuForm()

    return render(request,'menu.html',{'form' : form,}
    )


