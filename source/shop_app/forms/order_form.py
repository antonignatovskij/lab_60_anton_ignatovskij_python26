from django import forms

from shop_app.models import Product, Category, Cart, Order



class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name']