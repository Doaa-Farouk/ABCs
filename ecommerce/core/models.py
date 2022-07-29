from audioop import reverse
from distutils.command.upload import upload
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE, blank=False)
    phone = models.CharField(max_length= 12)
    CITIES= (
        ('1','Sanaa'),
        ('2','Taiz'),
        ('3','Ibb') ,
        ('4','Aden')
        )
    city = models.CharField(max_length=20, choices = CITIES)
    
    
    
class Category(models.Model):
    category_name= models.CharField(max_length=200)
    
    def __str__(self):
        return self.category_name
    
    
class Product(models.Model):
    name= models.CharField(max_length=300,verbose_name='اسم المنتج')
    category= models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='اسم الفئة')
    description=models.TextField(verbose_name='التفاصيل')
    price=models.FloatField(default=0.0,verbose_name='السعر')
    count=models.IntegerField(default=0,verbose_name='الكمية')
    image=models.ImageField(upload_to='images/',verbose_name='صورة المنتج')
    
    
    def get_add_to_cart_url(self):
        return reverse('core:add_to_cart',kwargs={
            'pk':self.pk
        })
        