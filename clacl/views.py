from django.shortcuts import render
from .forms import ClacForm

def home(request):
    result = 0
    if request.method == 'POST':
        form = ClacForm(request.POST)

        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            o = form.cleaned_data['c_choise']

            if o == '-':
                result = a - b
            elif o == '+':
                result = a + b
            elif o == '*':
                result = a * b
            else:
                result = a / b
    else:
        form = ClacForm()
    return render(request, 'clacl/home.html', {'form': form, 'result': result})