from django.shortcuts import render
import datetime

# Create your views here.

def wish_view(request):
    date = datetime.datetime.now()
    h = int(date.strftime('%H'))

    if h<12:
        msg = "Hello guest !!!, Very very Good Morning"
        
    elif h<16:
        msg = "Hello guest !!!, Very very Good Afternoon"

    elif h<21:
        msg = "Hello guest !!!, Very very Good Evening"

    else:
        msg = "Hello guest !!!, Very very Good Night"

    mydict = {'date': date, 'msg': msg}

    return render(request,'testapp/results.html', mydict)