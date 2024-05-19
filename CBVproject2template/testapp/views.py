from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class HelloworldTemplateView(TemplateView):
    template_name = 'testapp/home.html'
