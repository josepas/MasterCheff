from django.conf.urls import patterns, url
from . import views

urlpatterns = [

    url(r'^$', views.indice, name='indice'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout_view, name='logout'),
    url(r'^registro/', views.registro, name='registro')
]
