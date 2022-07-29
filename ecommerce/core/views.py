from django.contrib import messages
from django.shortcuts import redirect, render
from core.forms import *
from core.models import *

# Create your views here.
def index(request):
    products = Product.objects.all()[:6]
    categories = Category.objects.all()
    
    return render(request, 'core/index.html',{'products': products,
                                              'categories':categories})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
           
        else:
            messages.info(request, "failed")    
            form = ProductForm()
    form = ProductForm()
    return render(request, 'core/add_product.html', {'form':form})


def product_details(request,pk):
    product= Product.objects.get(pk=pk)
    # category= Category.objects.get(pk=pk)
    return render(request, 'core/product_details.html',{'product':product}#,{'category':category}
                  )