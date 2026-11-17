from django import forms

from shop_app.models import Product, Category, Cart, Order



class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name', 'mobile_phone', 'address']

        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'label': 'Имя заказчика'}),
            'mobile_phone': forms.TextInput(attrs={'class': 'form-control', 'label': 'Номер телефона'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'label': 'Адрес'})
        }