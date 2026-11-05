from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

def home(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('result')

    else:
        form = StudentForm()

    return render(request, 'students/home.html', {'form': form})

def result(request):
    student = Student.objects.all()
    return render(request, 'students/result.html', {'student': student})