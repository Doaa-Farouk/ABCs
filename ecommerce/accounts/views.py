from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from core.models import *
from django.contrib import messages

# from accounts.forms import *
# Create your views here.

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        logged_user = authenticate(username=username, password=password)
        if logged_user is not None:
            login(request, logged_user)
            # should be redirected to profile page
            return redirect('/')
        messages.info(request, 'فشل تسجيل الدخول , حاول مرة أخرى')
    return render(request, 'accounts/login.html')



def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        c_password = request.POST.get('c_password')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        
        if password == c_password:
            if User.objects.filter(username= username).exists():
                messages.info(request, 'اسم المستخدم موجود مسبقاً')
                return redirect('user_register') 
            elif User.objects.filter(email= email).exists():
                messages.info(request, 'البريد الالكتروني موجود مسبقاً')
                return redirect('user_register') 
            else:
                user = User.objects.create_user(username= username,email= email,password = password)                
                user.save()                    
                data = Customer(user= user, phone=phone, city= city)
                data.save()
                
                # login code
                logged_user = authenticate(username=username, password=password)
                if logged_user is not None:
                    login(request, logged_user)
                    # should be redirected to profile page
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



