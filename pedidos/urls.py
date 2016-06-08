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
    url(r'^verMenu/(?P<id>[0-9]+)$', views.verMenu, name='verMenu'),
    url(r'^restaurantesMenu/$', views.restaurantesMenu, name='restaurantesMenu'),
    url(r'^restaurantesPlatos/$', views.restaurantesPlatos, name='restaurantesPlatos'),
    url(r'^crearMenu/(?P<id>[0-9]+)/$', views.agregar_menu, name='agregar_menu'),
    url(r'^platos/(?P<id>[0-9]+)/$', views.agregar_platos, name='agregar_platos'),
    url(r'^usuariosRegistrados/$', views.usuariosRegistrados, name='usuariosRegistrados'),
    url(r'^restaurante/$', views.registroRestaurante, name='restaurante'),
    url(r'^proveedor/borrar/(?P<id>[0-9]+)/$', views.eliminar_servicio, name='eliminar_servicio'),
    url(r'^borrarPlato/(?P<id>[0-9]+)/$', views.eliminar_plato, name='eliminar_plato'),
    url(r'^editarPlato/(?P<id>[0-9]+)/$', views.editar_plato, name='editar_plato'),
    url(r'^usuariosRegistrados/ver/(?P<id>[0-9]+)/$', views.usuarioSeleccionado, name='usuarioSeleccionado'),
    url(r'^proveedor/$', views.agregar_servicios, name='agregar_servicios'),
    url(r'^registroRestaurante/$', views.registroRestaurante, name='registroRestaurante')
]
