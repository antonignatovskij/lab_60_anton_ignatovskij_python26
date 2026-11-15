from django import forms
from shop_app.models import Category


class ProductForm(forms.Form):
    name = forms.CharField(
        max_length=200,
        required=True,
        label='Наименование Товара',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    description = forms.CharField(
        max_length=500,
        required=False,
        label='Описание товара',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5', 'cols': '50'})
    )

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=True,
        label='Выберите категорию',
        empty_label='Выберите категорию',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    cost = forms.DecimalField(
        min_value=0.01,
        max_digits=7,
        decimal_places=2,
        required=True,
        label='Цена',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    image = forms.URLField(
        required=True,
        label='Ссылка на изображение',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    balance = forms.IntegerField(
        min_value=0,
        required=True,
        label='Колличество',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )



class CategoryForm(forms.Form):
    name = forms.CharField(
        max_length=60,
        required=True,
        label='Наименование Категеории',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    description = forms.CharField(
        max_length=500,
        required=False,
        label='Описание категории',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': '5', 'cols': '50'})
    )



class SearchForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        label='Поиск по названию',
        widget=forms.SearchInput(attrs={'class': 'form-control', 'placeholder': 'Введите название товара'}),
    )

