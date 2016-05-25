from .forms import FormaRegistro
from .models import Usuario
from django.contrib.auth.models import User
from django.shortcuts import render


# Aqui van las views/vistas

def indice(request):
    return render(request, 'base.html')


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
