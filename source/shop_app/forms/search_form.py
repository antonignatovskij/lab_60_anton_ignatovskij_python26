from django import forms



class SearchForm(forms.Form):
    search = forms.CharField(
        max_length=100,
        required=True,
        label='Поиск по названию',
        widget=forms.SearchInput(attrs={'class': 'form-control', 'placeholder': 'Введите название товара'}),
    )