from django import forms
from django_bootstrap5 import widgets

from shop_app.models import Product, Category

class TestForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'cost', 'image', 'balance']
        widgets = {
            'name': widgets.TextInput(attrs={'class': 'form-control'}),
            'description': widgets.Textarea(attrs={'class': 'form-control', 'rows': '5', 'cols': '50'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'cost': widgets.NumberInput()
        }


class ProductForm(forms.ModelForm):
    cost = forms.DecimalField(
        min_value=0.01,
        max_digits=7,
        decimal_places=2,
        label='Цена',
    )
    image = forms.URLField(label='Ссылка на изображение')
    balance = forms.IntegerField(min_value=0, label='Количество')

    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'cost', 'image', 'balance']

        labels = {
            'name': 'Наименование товара',
            'description': 'Описание товара',
            'category': 'Выберите категорию',
        }

        widgets = {
            'description': forms.Textarea(attrs={'rows': 5, 'cols': 50}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'




class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']

        labels = {
            'name': 'Наименование категории',
            'description': 'Описание категории',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'cols': 50,
            }),
        }



class SearchForm(forms.Form):
    search = forms.CharField(
        max_length=100,
        required=True,
        label='Поиск по названию',
        widget=forms.SearchInput(attrs={'class': 'form-control', 'placeholder': 'Введите название товара'}),
    )

