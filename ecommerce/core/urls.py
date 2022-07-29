from django import views
from core import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('add_product/', views.add_product, name='add_product'),
    path('product/<pk>', views.product_details, name='product_details'),
]