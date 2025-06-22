from django.shortcuts import render

# Create your views here.

# request.COOKIES[cookie_name] --COOKIES is a dictionary/dict object , get corresponding data/ get cookie from request object
# cookie is string type 
# request.COOKIES.get(cookie_name,default_value) : here get is one function of dict 
# response.set_cookie(cookie_name,cookie_value : add cookie to the response)


def count_view(request):

    count = int(request.COOKIES.get('count', 0))
    newcount = count+1
    response = render(request, 'testapp/results.html', {'count': newcount})
    # response.set_cookie('count', newcount)  #Temprary Cookies : it store in Browser
    response.set_cookie('count', newcount, max_age=160)  #Permanaent Cookies : It store in local machine
    return response

"""
2 types of cookie are available
- temprary cookie: once browser closed data / cookies gone (stored in browser)
- persistant/permanent cookie: if browser closed still cookie data/cookiw are availabe (store in our local machine)
"""
