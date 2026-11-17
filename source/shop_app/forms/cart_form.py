from django import forms

from shop_app.models import Cart



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
