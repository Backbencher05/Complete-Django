from typing import Any
from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import HttpResponse
# Create your views here.

class HelloworldClassView(View):
    def get(self,request):
        return HttpResponse('<h1>This Response is coming from Class basedview</h1>')
    
class HelloworldTemplateview(TemplateView):
    template_name = 'testapp/results.html'


class HelloworldTemplateContextView(TemplateView):
    template_name = 'testapp/emp.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Aditya'
        context['subject'] = 'Python'
        context['marks'] = 100
        return context
    

# Note: till now we have used 2 view classes
        # 1. View
        # 2. TemplateView

    # these are general view class 

# Now model related view so that we can Database to perform CURD operation
# 1. ListView --> R (To Read all record)
# 2. DetailView --> R (To get details of a particular rcord)
# 3. CreateView --> C
# 4. DeleteView --> D
# 5. UpdateView  --> U

# all are pre-define classes 

