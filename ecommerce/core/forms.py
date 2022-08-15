from core.models import CheckoutDetails, Product
from django import forms
from django.contrib.auth.models import User

class ProductForm(forms.ModelForm):
    class Meta:
        model= Product
        fields= '__all__'
        widgets= {
            'name' : forms.TextInput(attrs={'class':'user-box'}),
            'category' : forms.Select(attrs={'class':'user-box'}),
            'description' : forms.Textarea(attrs={'class':'user-box'}),
            'price' : forms.NumberInput(attrs={'class':'user-box'}),
            'count' : forms.NumberInput(attrs={'class':'user-box'}),
            'image' : forms.FileInput(attrs={'class':'user-box'}),
        }

class CheckoutForm(forms.ModelForm):
    class Meta:
        model= CheckoutDetails
        # first and last name must be provided here
        fields= ('phone', 'country', 'city', 'address', 'specific_address')
        widgets={
            'phone' : forms.TextInput(attrs={'class':'phone input'}),
            'country': forms.TextInput(attrs={'class':'country_name input'}),
            'city': forms.TextInput(attrs={'class':'city input'}),
            'address': forms.TextInput(attrs={'class':'address input'}),
            'specific_address': forms.TextInput(attrs={'class':'address input'}),
        }
            
        labels={
            'phone': 'التلفون',
            'country': 'الدولة',
            'city': 'المدينة',
            'address':'العنوان' ,
            'specific_address':'تفاصيل العنوان',
                
        }