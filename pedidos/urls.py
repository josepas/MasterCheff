from django.conf.urls import patterns, url
from . import views

urlpatterns = [

	url(r'^editarPerfil', views.editarPerfil, name='editarPerfil'),
	url(r'^perfil', views.perfil, name='perfil'),
    url(r'^$', views.indice, name='indice'),
    url(r'^login/', views.login, name='login'),
    url(r'^registro/', views.registro, name='registro' )
]
