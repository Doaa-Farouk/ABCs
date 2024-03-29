from django.contrib import messages
from django.shortcuts import redirect, render
from core.forms import *
from core.models import *
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404


# Create your views here.                                        
                                                
def index(request):
    products = Product.objects.all()[:30]
    images= Pictuers.objects.all()
    categories = Category.objects.all()
    
    
    return render(request, 'core/index.html',{'products': products,
                                              'images':images,
                                              'categories':categories
                                              })

def profile(request,username):
    categories = Category.objects.all()
    user= User.objects.get(username=username)
    if request.user.username == username:
        return render(request,'accounts/profile.html',{'user':user})
    else:
        raise Http404('PAGE IS NOT FOUND')     
           


def product_details(request,pk):
    product= Product.objects.get(pk=pk)
    images= Pictuers.objects.filter(product__pk=pk)
    category= Category.objects.filter(product__pk=pk)
    categories = Category.objects.all()
    return render(request, 'core/product_details.html',
                  {'product':product,
                   'images': images,
                   'category':category,
                   'categories':categories
                   })
    
                  
    
    
# @login_required(login_url='/accounts/ulogin/') 
def add_to_cart(request,pk):
    product= Product.objects.get(pk=pk)
    try:
        customer = request.user.customer
        print('found')
    except:
        device = request.COOKIES['device']
        customer, created = Customer.objects.get_or_create(device=device)
        print('not found')
    
    
    order, created = Order.objects.get_or_create(customer=customer, ordered=False)
    order_item, created= OrderItem.objects.get_or_create(
        product= product,
        order= order)
    
    # order_query set
    # order_qs= Order.objects.filter(customer=customer, ordered=False)
    # if order_qs.exists():
    #     order= order_qs[0]
    #     if order.items.filter(product__pk= pk).exists():
    #         order_item.quantity += 1
    #         order_item.save()
    #         return redirect('product_details',pk=pk)
        
    #     else:
    #         order.items.add(order_item)
    #         messages.info(request, 'تم إضافة المنتج')
    #         return redirect('product_details',pk=pk)
        
    # else:
    #     order_date= timezone.now()
    #     order= Order.objects.create(customer= customer, order_date=order_date)
    #     order.items.add(order_item)
    #     messages.info(request, 'تم إضافة المنتج')
    return redirect('product_details',pk=pk)

def orderlist(request):
    categories = Category.objects.all()
    
    if request.user.is_authenticated:
        if Order.objects.filter(user=request.user, ordered=False).exists():
            order = Order.objects.get(user=request.user, ordered=False)
            cart_items= order.cart_items_count
            context= {'cart_items':cart_items,"order": order,'categories':categories }
            return render(request, "core/orderlist.html", context)
        return render(request, "core/orderlist.html", {"message": "Your Cart is Empty"})
    else:
        order = ''
        return render(request, "core/orderlist.html", {"order": order, 'categories':categories})
    
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
                order_item.quantity -= 1
                order_item.save()
            else:
                order_item.delete()
            return redirect('orderlist')
        else:
            return redirect("orderlist")
    else:
        return redirect("orderlist")

@login_required(login_url='/accounts/ulogin/')      
def checkout(request):
    if CheckoutDetails.objects.filter(user=request.user).exists():
        return render(request, 'core/checkout.html')
    
    if request.method == 'POST':
        form= CheckoutForm(request.POST)
        if form.is_valid():
            phone = form.cleaned_data.get('phone')
            country= form.cleaned_data.get('country')
            city= form.cleaned_data.get('city')
            address= form.cleaned_data.get('address')
            specific_address= form.cleaned_data.get('specific_address')
            
            checkoutdetails= CheckoutDetails(
                user= request.user,
                phone= phone,
                country= country,
                city= city,
                address= address,
                specific_address= specific_address
            )
            checkoutdetails.save()
            form= CheckoutForm()
            messages.success(request, 'تم تأكيد الطلب بنجاح, سيتم توصيل الطلب إلى العنوان الذي قمت بإدخاله')
            return redirect('/')
        else:
            messages.info(request, 'failed')
            form= CheckoutForm()
            return render(request,'core/checkout.html',{'form':form})
    else:
        form= CheckoutForm()
        return render(request,'core/checkout.html',{'form':form})
    
def update_checkout(request, pk):
    obj = get_object_or_404(CheckoutDetails, pk= request.user.user_id)
    form = CheckoutForm(request.POST, instance=obj)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'core/checkout.html',{'form':form})

    # الحل انه نخلي الريكوست ياخذ المفتاح حق اليوزر من جدول العناوين بدل المفتاح حق العنوان نفسه
    
def clear_cart():
    pass