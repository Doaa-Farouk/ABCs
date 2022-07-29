
from core.models import Product
from django import forms

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
        