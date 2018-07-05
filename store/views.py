from django.shortcuts import render,redirect
#from.models import Store
from django.http import HttpResponse
#from django.contrib.auth.decorators import login_required
#from .import forms

def product_list(request):
    return HttpResponse("product list")

def product_detail(request):
    return HttpResponse("product details")
