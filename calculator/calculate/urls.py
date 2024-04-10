from django.urls import path
from .views import add, subtract, multiply, divide
urlpatterns = [
    path('add/<int:num1>/<int:num2>/', add, name = 'add'),
    path('subtract/<int:num1>/<int:num2>/', subtract, name = 'subtract'),
    path('multiply/<int:num1>/<int:num2>/', multiply, name = 'multiply'),
    path('divide/<int:num1>/<int:num2>/', divide, name = 'divide'),
]