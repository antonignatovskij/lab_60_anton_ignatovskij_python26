from django import forms

from shop_app.models import Product, Category, Cart, Order


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


class CartForm(forms.ModelForm):
    balance = forms.IntegerField(
        min_value=1,
        initial=1,
        widget=forms.NumberInput(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = Cart
        fields = ['balance']

    def clean_balance(self):
        total = self.instance.balance + self.cleaned_data['balance']
        if total > self.instance.product.balance:
            raise forms.ValidationError('Incorrect amount')
        return total


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['full_name']


class SearchForm(forms.Form):
    search = forms.CharField(
        max_length=100,
        required=True,
        label='Поиск по названию',
        widget=forms.SearchInput(attrs={'class': 'form-control', 'placeholder': 'Введите название товара'}),
    )

