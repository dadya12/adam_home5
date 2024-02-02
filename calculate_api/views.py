import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def calculated(request, tranzaction):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            a = int(data.get('A'))
            b = int(data.get('B'))
            if tranzaction == "add":
                finish = a + b
            elif tranzaction == "subtract":
                finish = a - b
            elif tranzaction == "multiply":
                finish = a * b
            elif tranzaction == "divide":
                if b == 0:
                    return JsonResponse({'error': 'Division by zero'}, status=400)
                finish = a // b
            else:
                return JsonResponse({'error': 'Что то пошло не так'}, status=400)
            return JsonResponse({'answer': finish})
        except (ValueError, KeyError):
            return JsonResponse({'error': 'Неверный тип данных'}, status=400)
        except ZeroDivisionError:
            return JsonResponse({"error": "Division by zero"}, status=400)

    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def add(request):
    return calculated(request, 'add')

@csrf_exempt
def subtract(request):
    return calculated(request, 'subtract')

@csrf_exempt
def multiply(request):
    return calculated(request, 'multiply')

@csrf_exempt
def divide(request):
    return calculated(request, 'divide')






