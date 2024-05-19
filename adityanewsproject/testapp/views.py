from django.shortcuts import render

# Create your views here.

def home_page_view(request):
    return render(request, 'testapp/home.html')


def movie_news_view(request):
    news1 = 'Devdas movie is not good'
    news2 = 'Salman updating Minimum 100 Cr Gurantee for his movie'
    news3 = 'Solani slowly getting curing'
    news4 = 'Amitabh bachan next movie is Thugs of Hindustan'
    news5 = 'Salman and katrina getting to marry soon'

    mydict = {'news1': news1, 'news2': news2, 'news3': news3, 'news4': news4, 'news5': news5}

    return render(request, 'testapp/mnews.html', mydict)