from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.

def contact(request):
    return render(request,'contact/index.html')

def submit_form(request):
    if request.method == 'POST':
        input_data = request.POST.get('input_data')
        return redirect('another_page')
    else:
        pass

def another_page(request):
    return render(request, 'another_page/another_page.html')