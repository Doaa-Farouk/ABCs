from django import forms
from core.models import Customer

class LoginForm(forms.ModelForm):
    class Meta:
        model= Customer
        fields= [
            'user',
            'phone'
        ]   
