from django.shortcuts import render, redirect

# Create your views here.
def task(request):
    return render(request, 'task/index.html')

def another_page(request):
    if request.method == 'POST':
        input_text = request.POST.get('input', '')
        combined_text = f'hello, {input_text}. Its sunny today'
        return render(request, 'another_page/index.html', {'combined_text': combined_text})
    else:
        return render(request, 'another_page/index.html')
