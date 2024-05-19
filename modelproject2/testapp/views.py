from django.shortcuts import render
from testapp.models import Employee_Regist

# Create your views here.

def Employee_view(request):
    employee = Employee_Regist.objects.all()
    print(employee)
    mydict = {'emplist': employee}
    print(mydict)
    return render(request, 'testapp/results.html', mydict)