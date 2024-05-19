from django.shortcuts import render
import datetime

# Create your views here.

def dynamic_template_views(request):
    date = datetime.datetime.now()
    name = "Ankit"
    roll_no = 101
    marks = 95
    dict = {'date':date,'Name': name, 'roll': roll_no, 'marks': marks}
    return render(request, 'testapp/results.html', context=dict)
