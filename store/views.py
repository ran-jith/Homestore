from django.shortcuts import render,redirect
from.models import Store
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
#from .import forms

def product_list(request):
    products = Store.objects.all().order_by('date')
    return render(request,'store/product_list.html',{ 'product':products })#render(request(always),path)#last create a dictionary to send data to templates

    #return HttpResponse("product list")

def product_detail(request):
    return HttpResponse("product details")
