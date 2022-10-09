from django import views
from cp import views
from django.urls import path


urlpatterns = [
    path('add_product/', views.add_product, name='add_product'),
    path('customers_orders/', views.customers_orders, name='customers_orders'),

]