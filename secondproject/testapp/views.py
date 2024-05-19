from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.

def datetime(request):
    date = 'hello'
    s = '</h1> The current Date and time at Server is:' + str(date) + '</h1>' 
    return HttpResponse(s)