from django.shortcuts import render

# Create your views here.

def name_view(request):
    return render(request, 'testapp/name.html')

# After submitting Name , read name provided by end user because to used in the future purpose
# add that response name/data to the cookie and display the age form

# because we have defined action=/age in name.html, so after submitting controll will come to age_view
def age_view(request):
    # Job of this age view is, 
    # read name entered by end user
    # save this name for the future purpose inside cookie 
    #  display age form
    name = request.GET['name']  
    #Reading data from name.html  
    # In the  Get request there is one text field named with name ,
    # whatever the value is there read and store in name variable that we have taken #name coming from 
    response = render(request, 'testapp/age.html', {'name': name})
    response.set_cookie('name', name)
    return response

def gf_view(request):
    # Job of this gf view is, 
    # read age entered by end user
    # save this name for the future purpose inside cookie 
    #  display gf form
    age = request.GET['age']
    name = request.COOKIES['name']
    response = render(request, 'testapp/gf.html',{'name': name})
    response.set_cookie('age', age)
    return response

def results_view(request):
    name = request.COOKIES['name']
    age = request.COOKIES['age']
    gf = request.GET['gf']
    mydict = {'name': name, 'gf': gf, 'age': age}
    response = render(request,'testapp/results.html', mydict)
    response.set_cookie('gf', gf)
    return response

def display_view(request):
    return render(request,'testapp/display.html')