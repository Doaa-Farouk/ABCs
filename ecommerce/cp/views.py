from django.shortcuts import render
from django.contrib import messages
from core.forms import *
from core.models import *
from django.http import Http404
# Create your views here.

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
           
        else:
            messages.info(request, "failed")    
            form = ProductForm()
    form = ProductForm()
    return render(request, 'cp/add_product.html', {'form':form})

def add_category(request):
    if request.method == 'POSt':
        pass

def customers_orders(request):
    if request.user.is_superuser:
        order= Order.objects.all()
        checkout_detail= CheckoutDetails.objects.all()
        return render(request, 'cp/customers_orders.html', 
                    {   
                        'order':order,
                        'checkout_detail':checkout_detail,
                    })
    else:
        raise Http404('PAGE IS NOT FOUND')