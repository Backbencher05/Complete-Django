from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
# from django.views.generic import View
# from django.http import HttpResponse
# # Create your views here.

# class HelloWorldView(View):
#     def get(self,request):
#         return HttpResponse('<h1> This is from Class Based View</h1>')

class HelloWorldView(View):
    def get(self,request):
        return HttpResponse('<h1> This response is coming from Classs based view</h1>')