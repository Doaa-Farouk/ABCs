from django.contrib import messages
from django.shortcuts import redirect, render
from core.forms import *
from core.models import *
from django.utils import timezone

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
    
    
    
def add_to_cart(request,pk):
    product= Product.objects.get(pk=pk)
    order_item, created= OrderItem.objects.get_or_create(
        product= product,
        user = request.user,
        ordered= False 
    )
    # order_query set
    order_qs= Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order= order_qs[0]
        if order.items.filter(product__pk= pk).exists():
            order_item.quantity += 1
            order_item.save()
            return redirect('product_details',pk=pk)
        
        else:
            order.items.add(order_item)
            # order_item.save()
            messages.info(request, 'تم إضافة المنتج')
            return redirect('product_details',pk=pk)
        
    else:
        order_date= timezone.now()
        order= Order.objects.create(user= request.user, order_date=order_date)
        order.items.add(order_item)
        messages.info(request, 'تم إضافة المنتج')
        return redirect('product_details',pk=pk)
        