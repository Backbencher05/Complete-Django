from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def good_morning_view(requaest):
    return HttpResponse('<h1> Hello friends good morning</h1>')


def good_afternoon_view(requaest):
    return HttpResponse('<h1> Hello friends good Afternoon</h1>')

def good_evening_view(requaest):
    return HttpResponse('<h1> Hello friends good evening</h1>')


