from django.shortcuts import render
from testapp.models import Books
from django.views.generic import ListView, DetailView

# Create your views here.

# function based view
def listview(request):
    book = Books.objects.all
    return render(request, 'testapp/all.html', {'book': book})

# Now model related view so that we can Database to perform CURD operation
# 1. ListView --> R (To Read all record)
# 2. DetailView --> R (To get details of a particular rcord)
# 3. CreateView --> C
# 4. DeleteView --> D
# 5. UpdateView  --> U

# all are pre-define classes 
# Now we don't have to specify and template explacitely
    # listview  contact default template
    # so, modelclassname_list.html (all in lowe case)
    # default template: books_list.html
    # to get all the information, we have to create context object 
    # so
    # default template: books_list.html
    # default context object: books_list


# Class Based view

# 1. ListView 
# We can use ListView to list of all records present in the database table.

class BookListView(ListView):
    model = Books
    # default template: books_list.html
    # default context object: books_list

    
# 2. Detail View 
# to get  details of a particular record, we should go for DetailView.

class BookdetailView(DetailView):
    model = Books
    # default template: books_detail.html
    # default context object : books or object
