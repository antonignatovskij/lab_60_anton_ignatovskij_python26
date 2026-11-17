from django import forms

from shop_app.models import Category



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