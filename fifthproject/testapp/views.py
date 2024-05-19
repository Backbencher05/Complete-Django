from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def first_view(request):
    return HttpResponse('<h1> Response from first view')

def second_view(request):
    return HttpResponse('<h1> Response from second view')

def third_view(request):
    return HttpResponse('<h1> Response from third view')

def fourth_view(request):
    return HttpResponse('<h1> Response from fourth view')

def fifth_view(request):
    return HttpResponse('<h1> Response from fifth view')