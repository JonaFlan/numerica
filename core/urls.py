from django.urls import path
from django.urls import path
from .views import home, calcular_regresion, calcular_derivada, regresion, derivadas, formularioR, tabla_derivadas

urlpatterns = [
    path('', home, name='home'),
    path('derivadas/calculadora/', derivadas, name='calculadora_derivadas'),
    path('derivadas/tabla/', tabla_derivadas, name='tabla_derivadas'),
    path('regresion/', regresion, name='regresion'),
    path('calcular_regresion/', calcular_regresion, name='calcular_regresion'),
    path('formulario/', formularioR, name='formularioR'),
    path('calcular_derivada/', calcular_derivada, name='calcular_derivada'),

]