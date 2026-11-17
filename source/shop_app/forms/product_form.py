from django import forms

from shop_app.models import Product


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