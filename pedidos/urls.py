from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.login, name='registro'),
    url(r'^$', views.indice, name='registro'),
    url(r'^registro/$', views.registro, name='registro' ),
    url(r'^registro/restaurante/$', views.registroRestaurante, name='regRestaurante')

]