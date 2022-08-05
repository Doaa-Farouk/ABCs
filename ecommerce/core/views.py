from django.contrib import messages
from django.shortcuts import redirect, render
from core.forms import *
from core.models import *
from django.utils import timezone
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    products = Product.objects.all()[:30]
    categories = Category.objects.all()
    
    return render(request, 'core/index.html',{'products': products,
                                              'categories':categories})

def profile(request,username):
    user= User.objects.get(username=username)
    return render(request,'accounts/profile.html',{'user':user})
  
        

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

def orderlist(request):
    if Order.objects.filter(user=request.user, ordered=False).exists():
        order = Order.objects.get(user=request.user, ordered=False)
        return render(request, "core/orderlist.html", {"order": order})
    return render(request, "core/orderlist.html", {"message": "Your Cart is Empty"})



def add_item(request,pk):
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
            if order_item.quantity < product.count:
                order_item.quantity += 1
                order_item.save()
                return redirect('orderlist')
            else:
                messages.info(request, 'لقد نفذت الكمية')
                return redirect("orderlist")
        else:
            order.items.add(order_item)
            messages.info(request, 'تم إضافة المنتج')
            return redirect('orderlist')
        
    else:
        order_date= timezone.now()
        order= Order.objects.create(user= request.user, order_date=order_date)
        order.items.add(order_item)
        messages.info(request, 'تم إضافة المنتج')
        return redirect('orderlist')
    
    
def remove_item(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_qs= Order.objects.filter(user= request.user, ordered= False)
    if order_qs.exists():
        order= order_qs[0]
        if order.items.filter(product__pk=pk).exists():
            order_item= OrderItem.objects.filter(
                product= item,
                user= request.user,
                ordered= False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -=1
                order_item.save()
            else:
                order_item.delete()
            return redirect('orderlist')
        else:
            return redirect("orderlist")
    else:
        return redirect("orderlist")