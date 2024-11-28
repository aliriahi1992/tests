from django.shortcuts import render
from .forms import CalculateForm

def calculate(request):
    if request.method == 'POST':
        form = CalculateForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            result = (num1 + num2)*100
            return render(request, 'calculator/result.html', {'result': result})
    else:
        form = CalculateForm()
    return render(request, 'calculator/calculate.html', {'form': form})