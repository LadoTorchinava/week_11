from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def add(request, num1, num2):
    result = num1 + num2
    return render(request, 'add/index.html', {'num1': num1, 'num2': num2, 'result': result})

def subtract(request, num1, num2):
    result = num1 - num2
    return render(request, 'subtract/index.html', {'num1': num1, 'num2': num2, 'result': result})

def multiply(request, num1, num2):
    result = num1 * num2
    return render(request, 'multiply/index.html', {'num1': num1, 'num2': num2, 'result': result})


def divide(request, num1, num2):
    result = num1 / num2
    return render(request, 'divide/index.html', {'num1': num1, 'num2': num2, 'result': result})




   