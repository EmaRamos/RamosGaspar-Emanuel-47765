from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import *

# Create your views here.

class ProductsList(ListView):
    model= Products

    def get_queryset(self):
        query = self.request.GET.get('name', '') 
        
        if query:
        
            return Products.objects.filter(name__icontains= query)
        
        return Products.objects.all()

class ProductsDetail(DetailView):
    model= Products

class ProductsCreate(LoginRequiredMixin, CreateView):
    model= Products
    success_url= reverse_lazy('Home')
    fields= ['name', 'description', 'price', 'category', 'image', 'is_sale', 'sale_price']

class ProductsUpdate(LoginRequiredMixin, UpdateView):
    model= Products
    success_url= reverse_lazy('Home')
    fields= ['name', 'description', 'price', 'category', 'image', 'is_sale', 'sale_price']

class ProductsDelete(LoginRequiredMixin, DeleteView):
    model= Products
    success_url= reverse_lazy('Home')

@login_required
def checkout(request):
    return render(request, 'store/checkout.html')

def about(request):
    return render(request, 'store/about.html')