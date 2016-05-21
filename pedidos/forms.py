from django import forms

class FormaRegistro(forms.Form):
    username = forms.CharField(label='Usuario', max_length=100)
    nombres = forms.CharField(label='Nombres', max_length=100)
    apellidos = forms.CharField(label='Apellidos', max_length=100)
    passwd = forms.CharField(label='Contrase;a', widget=forms.PasswordInput())
    cedula = forms.IntegerField(min_value=1, max_value=120000000) # aqui no diferenciamos entre extranjeros y venezolanos
    fecha_nac = forms.DateField(input_formats=('%d-%m-%Y','%Y-%m-%d'))
