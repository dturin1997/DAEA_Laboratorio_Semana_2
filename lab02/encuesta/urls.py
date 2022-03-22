from django.urls import path

from . import views

app_name = 'encuesta'

urlpatterns = [
    # ex: /encuesta/
    path('', views.index, name='index'),
    path('ejercicio1', views.ejercicio1, name='ejercicio1'),
    path('enviar', views.enviar, name='enviar'),
    path('calcular', views.calcular, name='calcular'),
]