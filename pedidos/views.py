from .forms import FormaRegistro, FormaRestaurante, CrearMenuForm
from .models import Usuario


from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as mch_login
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from django.core.urlresolvers import reverse


def editarPerfil(request):
    return render(request, 'editarPerfil.html')

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
    # falta chequear si ya esta el usuario creado!
    # NO logre que agarre fechas distintas a YYYY-MM-DD!

    mensaje = None
    if request.method == 'POST':

        form = FormaRegistro(request.POST)
        if form.is_valid():

            u = User.objects.create_user(request.POST["username"],
                'lennon@thebeatles.com', 
                request.POST["passwd"]
            )
            u.first_name=request.POST["nombres"]
            u.last_name=request.POST["apellidos"]
            u.save()
            nuevoU = Usuario(perfil=u, 
                            cedula=request.POST["cedula"],
                            fecha_nac=request.POST["fecha_nac"]
            )
            nuevoU.save()

            mensaje = "Creado con exito!"
            form = FormaRegistro()


    else:
        form = FormaRegistro()

    return render(request, 'registro.html', {'form': form, 'mensaje':mensaje})


def registroRestaurante(request):
    if request.method == 'POST':
        form = FormaRestaurante(request.POST)
        if form.is_valid():
            pass

    else:
        form = FormaRestaurante() 

    return render(request, 'registroRestaurante.html', {'form': form})

def menu_crear(request):
    form = CrearMenuForm()
    if request.method == 'POST':
        form = CrearMenuForm(request.POST)
        if form.is_valid():
            menu = Menu(
                nombre = form.cleaned_data['nombre'], 
                restaurante = Restaurante.objects.get(nombre = form.cleaned_data['restaurante']))
            
            menu.save()
            menu.productos = form.cleaned_data['productos']
            menu.save()
            
            return render(request, 'menu.html', {'mensaje' : "Se ha creado el menu"})
    
    return render(
        request,
        'menu.html',
        {
         'form' : form,
         'putanga' : "putas baratas de pueblo"
        }
    )

def restaurante_crear(request):
    form = FormaRestaurante()
    if request.method == 'POST':
        form = CrearMenuForm(request.POST)
        if form.is_valid():
            menu = Menu(
                nombre = form.cleaned_data['nombre'])
            menu.save()
            return render(request, 'menu.html', {'mensaje' : "Se ha creado el menu"})
    
    return render(
        request,
        'menu.html',
        {
         'form' : form,
         'putanga' : "putas baratas de pueblo"
        }
    )


