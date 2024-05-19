from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def greet_view(request):
    return HttpResponse('<h1> Hello Aditya how are you</h1>' )
