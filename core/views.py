import json
import logging
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import realizar_regresion
import sympy as sp

# Configurar el registro
logger = logging.getLogger(__name__)

def home(request):
    return render(request, 'core/index.html', {'hide_navbar': True})

def derivadas(request):
    return render(request, 'core/derivadas.html')

def regresion(request):
    return render(request, 'core/regresion.html')

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json

@csrf_exempt
def calcular_regresion(request):
    if request.method == 'POST':
        try:
            # Obtener la IP del usuario
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]
            else:
                ip = request.META.get('REMOTE_ADDR')
            
            # Imprimir la IP del usuario
            print(f"IP del usuario: {ip}")

            data = json.loads(request.body.decode('utf-8'))
            result = realizar_regresion(data)
            print(result)
            return JsonResponse(result)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)


def formularioR(request):
    return render(request, 'core/formularioR.html')

@csrf_exempt
def calcular_derivada(request):
    if request.method == 'POST':
        funcion = request.POST.get('funcion', '')
        try:
            x = sp.symbols('x')
            expr = sp.sympify(funcion.replace('^', '**'))
            derivada = sp.diff(expr, x)
            
            # Formatear las expresiones en LaTeX
            funcion_original_latex = sp.latex(expr).replace('**', '^')
            derivada_latex = sp.latex(derivada).replace('**', '^')
            
            return JsonResponse({'success': True, 'funcion_original': funcion_original_latex, 'derivada': derivada_latex})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Método no permitido.'})

def tabla_derivadas(request):
    return render(request, 'core/tabla_derivadas.html')
