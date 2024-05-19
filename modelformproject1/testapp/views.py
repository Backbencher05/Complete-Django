from django.shortcuts import render
from . import forms
# Create your views here.

def student_view(request):
    form = forms.StudentForm()
    # print("hellllo", form)
    if request.method =='POST':
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print("Data Saved")
    return render(request, 'testapp/results.html', {'form': form})