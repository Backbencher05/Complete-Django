from django.shortcuts import render, redirect
from testapp.models import Employee
from testapp.forms import EmployeeForm
# from django.http import HttpResponseRedirect
# Create your views here.

# CRUD operations

# 1. R: Retreave


def retreave_view(request):
    # get all the data
    employee = Employee.objects.all()
    return render(request, 'testapp/home.html', {'employee': employee})


# 2. C: create or insert
# To add Record let create one form, so that Employee can enter the information
# recomended : model based form 
def create_view(request):
    form = EmployeeForm() 

    if request.method == 'POST':
        # create form object 
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'testapp/create.html', {'form': form})