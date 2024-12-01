from django.shortcuts import render
from .forms import CalculateForm
import google.generativeai as genai
import requests

def calculate(request):
    if request.method == 'POST':
        form = CalculateForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            
            # دریافت کلید API از تنظیمات یا دیتابیس
            GOOGLE_API_KEY = 'AIzaSyAxFcWDhELaj8iR8QQkGLfrLSdK33yyn-4'  # یا استفاده از userdata.get('API_KEY_1')
            genai.configure(api_key=GOOGLE_API_KEY)
            
            # انتخاب مدل و ارسال درخواست به Gemini
            model = genai.GenerativeModel('gemini-pro')
            
            # فرض می‌کنیم که می‌خواهیم از دو عدد برای تولید محتوای خاص استفاده کنیم
            prompt = "صفات و ویژگی های یک دختر مهربان و با وفا و با وقار رو برام شرح بده"
            response = model.generate_content(prompt)

            # اینجا باید پاسخ مدل را پردازش کنید
            result = response.text
            
            return render(request, 'calculator/result.html', {'result': result})
    else:
        form = CalculateForm()
    
    return render(request, 'calculator/calculate.html', {'form': form})
