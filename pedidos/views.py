from .forms import FormaRegistro, FormaRestaurante
from .models import Usuario


from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render



def indice(request):
    return render(request, 'base.html')


def login(request):
    


    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
            else:
                pass
        mensaje = 'Hubo problemas con el login'

    else:
        pass

    return render(request, 'login.html')


def registro(request):

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

    else:
        form = FormaRegistro()

    return render(request, 'registro.html', {'form': form})


def registroRestaurante(request):
    if request.method == 'POST':
        form = FormaRestaurante(request.POST)
        if form.is_valid():
            pass

    else:
        form = FormaRestaurante() 

    return render(request, 'registroRestaurante.html', {'form': form})





