from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import math

def home(request):
    return render(request, 'core/home.html')

def calcular(request):
    if request.method == 'POST':
        operacao = request.POST['operacao']
        num1 = float(request.POST['num1'])
        num2 = float(request.POST['num2'])
        resultado = None
        
        if operacao == 'soma':
            resultado = num1 + num2
        elif operacao == 'subtracao':
            resultado = num1 - num2
        elif operacao == 'multiplicacao':
            resultado = num1 * num2
        elif operacao == 'divisao':
            resultado = num1 / num2
        elif operacao == 'raiz_quadrada':
            resultado = math.sqrt(num1)
        elif operacao == 'potencia':
            resultado = num1 ** num2
        
        context = {
            'resultado': resultado,
        }
        
        return render(request, 'core/home.html', context)