from unicodedata import category
from django.contrib import admin
from core.models import *
# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Pictuers)
admin.site.register(CheckoutDetails)
admin.site.register(Customer)

