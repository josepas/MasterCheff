from django.conf.urls import patterns, url
from . import views

urlpatterns = [

    url(r'^$', views.indice, name='indice'),
	url(r'^perfil/$', views.perfil, name='perfil'),
    url(r'^perfil/editar/(?P<userID>[0-9]+)/$', views.editar_perfil, name='editar_perfil'),
    url(r'^perfil/billetera/(?P<userID>\d+)/$', views.gestionar_billetera, name='gestionar_billetera'),

    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^registro/$', views.registro, name='registro'),
    url(r'^registroCliente/$', views.registroCliente, name='registroCliente'),
    url(r'^registroProveedor/$', views.registroProveedor, name='registroProveedor'),
    url(r'^listasMenu/(?P<id>[0-9]+)/(?P<idmenu>[0-9]+)$', views.listasMenu, name='listasMenu'),
    url(r'^restaurantesMenu/$', views.restaurantesMenu, name='restaurantesMenu'),
    url(r'^restaurantesPlatos/$', views.restaurantesPlatos, name='restaurantesPlatos'),
    url(r'^crearMenu/(?P<id>[0-9]+)/$', views.agregar_menu, name='agregar_menu'),
    url(r'^platos/(?P<id>[0-9]+)/$', views.agregar_platos, name='agregar_platos'),
    url(r'^usuariosRegistrados/$', views.usuariosRegistrados, name='usuariosRegistrados'),
    url(r'^restaurante/$', views.registroRestaurante, name='restaurante'),
    url(r'^proveedor/borrar/(?P<id>[0-9]+)/$', views.eliminar_servicio, name='eliminar_servicio'),

    url(r'^borrarPlato/(?P<id>[0-9]+)/$', views.eliminar_plato, name='eliminar_plato'),
    url(r'^borrarPlatoMenu/(?P<id>[0-9]+)/(?P<idmenu>[0-9]+)/(?P<idplato>[0-9]+)/$', views.eliminar_plato_menu, name='eliminar_plato_menu'),

    url(r'^borrarMenu/(?P<id>[0-9]+)/$', views.eliminar_menu, name='eliminar_menu'),
    url(r'^mostrarMenu/(?P<id>[0-9]+)/$', views.mostrar_menu, name='mostrar_menu'),
    url(r'^editarMenu/(?P<id>[0-9]+)/(?P<idmenu>[0-9]+)/$', views.agregar_menu_platos, name='agregar_menu_platos'),
    url(r'^mostrarMenuActual/(?P<id>[0-9]+)/$', views.mostrar_menu_actual, name='mostrar_menu_actual'),
    url(r'^editarPlato/(?P<id>[0-9]+)/$', views.editar_plato, name='editar_plato'),
    url(r'^usuariosRegistrados/ver/(?P<id>[0-9]+)/$', views.usuarioSeleccionado, name='usuarioSeleccionado'),
    url(r'^proveedor/$', views.agregar_servicios, name='agregar_servicios'),
    url(r'^registroRestaurante/$', views.registroRestaurante, name='registroRestaurante'),
    url(r'^seleccionarMenuActual/(?P<id>[0-9]+)/$', views.seleccionar_menu_actual, name='seleccionar_menu_actual'),

    url(r'^agregarPlatoPedido/(?P<idPlato>[0-9]+)/$', views.agregar_plato_pedido, name='agregar_plato_pedido'),
    url(r'^pedidos/(?P<idRestaurante>[0-9]+)/$', views.mostrar_pedidos, name='mostrar_pedidos'),
    url(r'^pagarPedidos/$', views.pagar_pedido, name='pagar_pedido'),
    url(r'^cancelarPedidos/$', views.cancelar_pedido, name='cancelar_pedido'),
    url(r'^notificaciones/$', views.agregar_notificacion, name='agregar_notificacion'),
    url(r'^notificaciones/(?P<id>[0-9]+)/$', views.eliminar_notificacion, name='eliminar_notificacion'),
    url(r'^estatusFinanciero/$', views.egresos_ingresos, name='egresos_ingresos'),
    url(r'^sugerenciasAdministrador/$', views.mostrar_sugerencias, name='mostrar_sugerencias'),
    url(r'^sugerenciasCliente/$', views.agregar_sugerencia, name='agregar_sugerencia'),
    url(r'^sugerenciasCliente/(?P<id>[0-9]+)/$', views.eliminar_sugerencia, name='eliminar_sugerencia')
]
