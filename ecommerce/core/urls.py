from django import views
from core import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('add_product/', views.add_product, name='add_product'),
    path('product/<pk>', views.product_details, name='product_details'),
    path('add_to_cart/<pk>', views.add_to_cart, name='add_to_cart'),
    path('profile/<username>', views.profile, name='profile'),
    path('orderlist', views.orderlist, name='orderlist'),
    path('add_item/<pk>', views.add_item, name='add_item'),
    path('remove_item/<pk>', views.remove_item, name='remove_item'),
    path('checkout', views.checkout, name='checkout'),
    path('update_checkout', views.update_checkout, name='update_checkout'),
    path('customers_orders', views.customers_orders, name='customers_orders'),
]