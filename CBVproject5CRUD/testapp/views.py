from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from testapp.models import Company
# Create your views here.


class CompanyListView(ListView):
    model = Company
    #default template_name is company_list.html
    #defult context_object_name is company_list

class CompanydetailView(DetailView):
    model = Company
    #default template_name is company_detail.html 
    # #defult context_object_name is company or object

class ComapnycreateView(CreateView):
    model = Company
    