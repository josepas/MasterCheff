from django.conf.urls import patterns, url
from . import views

urlpatterns = [

    url(r'^$', views.indice),
    url(r'^login/', views.login),
    url(r'^registro/', views.registro, name='registro' )
]