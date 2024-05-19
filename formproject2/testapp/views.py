from django.shortcuts import render
from . import forms
# Create your views here.

def thankyou_view(request):
    return render(request, 'testapp/thankyou.html')

def feedback_view(request):
    form = forms.Studentfeedback()
    print("hello",request)
    if request.method == 'POST':
        form = forms.Studentfeedback(request.POST)
        if form.is_valid():
            print('Form validation succesfull and printing data')
            print('Name: ', form.cleaned_data['name'])
            print('Roll No : ', form.cleaned_data['rollno'])
            print('Email_id: ', form.cleaned_data['email'])
            print('Feedback: ', form.cleaned_data['feedback'])
            return thankyou_view(request)
        
    return render(request, 'testapp/results.html', {'form': form})