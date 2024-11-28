from django import forms

class CalculateForm(forms.Form):
    num1 = forms.IntegerField(label='عدد اول')
    num2 = forms.IntegerField(label='عدد دوم')