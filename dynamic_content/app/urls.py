from django.urls import path
from.views import task, another_page

urlpatterns = [
    path('task/', task, name ='task'),
    path('result/', another_page, name ='result'),
]
