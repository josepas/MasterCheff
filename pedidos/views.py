from .forms import FormaRegistro, FormaRestaurante
from .models import Usuario


from django.contrib.auth import authenticate
from django.contrib.auth import login as mch_login
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from django.core.urlresolvers import reverse


def login(request):
    return render(request, 'login.html')

def indice(request):
    
    return render(request, 'base.html')


def login(request):

    if request.method == 'POST':
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                mch_login(request, user)
                return redirect('indice')

        mensaje = 'Hubo problemas con el login'

    return render(request, 'login.html')


def registro(request):
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
            mensaje = ""


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





