from django.conf.urls import patterns, url
from . import views

urlpatterns = [

    url(r'^$', views.indice, name='indice'),
	url(r'^perfil/$', views.perfil, name='perfil'),
    url(r'^perfil/editar/(?P<userID>[0-9]+)/$', views.editar_perfil, name='editar_perfil'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^registro/$', views.registro, name='registro'),
    url(r'^registroCliente/$', views.registroCliente, name='registroCliente'),
    url(r'^registroProveedor/$', views.registroProveedor, name='registroProveedor'),
    url(r'^crearMenu/$', views.crearMenu, name='crearMenu'),
    url(r'^verMenu/$', views.verMenu, name='verMenu'),
    url(r'^usuariosRegistrados/$', views.usuariosRegistrados, name='usuariosRegistrados'),
    url(r'^restaurante/$', views.registroRestaurante, name='restaurante'),
    url(r'^proveedor/borrar/(?P<id>[0-9]+)/$', views.eliminar_servicio, name='eliminar_servicio'),
    url(r'^proveedor/$', views.agregar_servicios, name='agregar_servicios')
]
