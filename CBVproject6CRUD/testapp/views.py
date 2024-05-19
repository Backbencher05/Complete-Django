from django.shortcuts import render
from testapp.models import Company
from django.views.generic import ListView,DetailView,CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

class CompanylistView(ListView):
    model = Company

class CompanydetailView(DetailView):
    model = Company

class CompanyCreateView(CreateView):
    model = Company
    fields = ['name', 'location', 'ceo']

class CompanyUpdateView(UpdateView):
    model = Company
    # which fields you want to  update 
    fields = ['ceo', 'location']

class CompanyDeleteView(DeleteView):
    model = Company
    # after deleting the record which page target page we have to go 
    # for that one lazy url concept is there
    # let after delete we want to land into home page
    # let give the name to our home page url "companies"
    success_url = reverse_lazy('companies')
