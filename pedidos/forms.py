from django import forms

class FormaRegistro(forms.Form):
    nombres = forms.CharField(label='Nombres', max_length=100)
    apellidos = forms.CharField(label='Apellidos', max_length=100)
    cedula = forms.IntegerField(min_value=1, max_value=120000000) # aqui no diferenciamos entre extranjeros y venezolanos
    fecha_nac = forms.DateField()
