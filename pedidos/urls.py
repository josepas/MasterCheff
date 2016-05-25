from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.indice, name='indice'),
    url(r'^registro/$', views.registro, name='registro' ),
    url(r'^registro/restaurante/$', views.registroRestaurante, name='regRestaurante')

]