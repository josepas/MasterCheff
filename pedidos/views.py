from .forms import FormaRegistro
from django.shortcuts import render


# Aqui van las views/vistas

def indice(request):
    return render(request, 'indice.html')



def registro(request):
    if request.method == 'POST':
        print(request.POST)
        form = FormaRegistro(request.POST)
    else:
        form = FormaRegistro()

    return render(request, 'registro.html', {'form': form})
