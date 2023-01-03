from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from core.models import *
from django.contrib import messages

# Create your views here.

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        logged_user = authenticate(username=username, password=password)
        if logged_user is not None:
            login(request, logged_user)
            return redirect('/')
        messages.info(request, 'فشل تسجيل الدخول , حاول مرة أخرى')
    return render(request, 'accounts/login.html')



def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        c_password = request.POST.get('c_password')
        email = request.POST.get('email')
        
        if password == c_password:
            if User.objects.filter(username= username).exists():
                messages.info(request, 'اسم المستخدم موجود مسبقاً')
                return redirect('user_register') 
            elif User.objects.filter(email= email).exists():
                messages.info(request, 'البريد الالكتروني موجود مسبقاً')
                return redirect('user_register') 
            else:
                user = User.objects.create_user(username= username,email= email,password = password, first_name= first_name, last_name= last_name)                
                user.save()   
                customer = Customer.objects.create(user= user,device= request.COOKIES['device'])     
                customer.save()            
                
                # login code
                logged_user = authenticate(username=username, password=password)
                if logged_user is not None:
                    login(request, logged_user)
                    return redirect('/')
                
        else:
            messages.info(request, 'كلمات المرور غير متطابقة')  
            return redirect('user_register')
            
    else:
        print('method is not post')
         
    
    return render(request, 'accounts/register.html')



def user_logout(request):
    logout(request)
    return redirect('/')



