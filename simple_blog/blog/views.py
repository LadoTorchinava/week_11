from django.shortcuts import render

info = [
    {'title': "motivation", 'name': "lasha", 'text' : "just do it" },
    {'title': "response", 'name': "lado", 'text' : "i will try" },
    {'title': "disappointment", 'name': "lasha", 'text' : "tfuiii" },
]
# Create your views here.
def task(request):
    return render(request, 'task/blog.html', {'info': info})