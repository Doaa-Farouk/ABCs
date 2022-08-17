from audioop import reverse
from email.mime import image
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CheckoutDetails(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    phone= models.CharField(max_length= 12)
    country= models.CharField(max_length=30)
    city= models.CharField(max_length=30)
    address= models.CharField(max_length=200)
    specific_address= models.CharField(max_length=200)
    
    def __str__(self):
        return self.user.username
    
    
class Category(models.Model):
    category_name= models.CharField(max_length=200)
    
    def __str__(self):
        return self.category_name
    
class Pictuers(models.Model):
    image=models.ImageField(upload_to='images/',verbose_name='صورة المنتج',null= True)
    product=models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name=' المنتج',default=1)

    def __str__(self):
        return self.image.url
    
class Product(models.Model):
    name= models.CharField(max_length=300,verbose_name='اسم المنتج')
    category= models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='اسم الفئة')
    description=models.TextField(verbose_name='التفاصيل')
    price=models.FloatField(default=0.0,verbose_name='السعر')
    count=models.IntegerField(default=0,verbose_name='الكمية')    
    
    def get_add_to_cart_url(self):
        return reverse('core:add_to_cart',kwargs={
            'pk':self.pk
        })

    def __str__(self):
        return self.name
    
    
class OrderItem(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, null=False , blank=False)
    ordered= models.BooleanField(default=False)
    product= models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity= models.IntegerField(default=1)
    
    def __str__(self):
        return f"{self.quantity} of {self.product.name}"
    
    def item_total_price(self):
        return self.quantity * self.product.price
    
    def final_price(self):
        return self.item_total_price()

    
class Order(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, null=False , blank=False)
    items= models.ManyToManyField(OrderItem)
    start_date= models.DateTimeField(auto_now_add=True)
    order_date= models.DateTimeField()
    order_id= models.CharField(max_length=100, null=True, blank=True, default=None, unique=True)
    ordered= models.BooleanField(default=False)
    delivered= models.BooleanField(default=False)
    received= models.BooleanField(default=False)
    date_of_payment= models.DateTimeField(auto_now_add=True)
    
    
    def save(self,*args,**kwargs):
        if self.order_id is None and self.date_of_payment and self.id :
             self.order_id= self.date_of_payment.strftime('PYDA%Y%m%dONT') + str(self.id)
        return super().save(*args,**kwargs)
    
    def __str__(self):
        return self.user.username
    
    def total_price(self):
        total=0
        for order_item in self.items.all():
            total += order_item.final_price()
        return total
    
    def total_count(self):
        order= Order.objects.get(pk=self.pk)
        return order.items.count()
