from django.shortcuts import render
from . import forms
# Create your views here.

def forms_view(request):
    form = forms.StudentForm()
    return render(request, 'testapp/results.html', {'form': form})
