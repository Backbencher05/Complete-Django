from django.shortcuts import render
from testapp.forms import MovieForm
from testapp.models import Movie

# Create your views here.

def index_view(request):
    return render(request, 'testapp/home.html')


def add_movie_view(request):
    form = MovieForm()
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            print("form saved")
        return index_view(request)

    return render(request, 'testapp/add_movie.html', {'form': form})


def list_movie_view(request):
    list_movie = Movie.objects.all()
    print("list", list_movie)
    return render(request, 'testapp/listmovie.html', {'list_movie': list_movie})