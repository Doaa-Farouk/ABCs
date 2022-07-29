from django import views
from accounts import views
from django.urls import path

urlpatterns = [
    path('ulogin/', views.user_login, name='user_login'),
    path('uregister/', views.user_register, name='user_register'),
    path('ulogout/', views.user_logout, name='user_logout'),
]