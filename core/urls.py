from django.urls import path
from django.urls import path
from .views import home, calcular_regresion, regresion, derivadas, formularioR, formularioD

urlpatterns = [
    # path('', home, name='home'),
    path('derivadas/', derivadas, name='derivadas'),
    path('', regresion, name='regresion'),
    path('calcular_regresion/', calcular_regresion, name='calcular_regresion'),
    path('formulario/', formularioR, name='formularioR'),
    path('formularioD/', formularioD, name='formularioD'),
]