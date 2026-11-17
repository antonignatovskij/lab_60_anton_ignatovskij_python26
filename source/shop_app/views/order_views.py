from django.shortcuts import redirect
from django.views.generic import View

from shop_app.forms import OrderForm
from shop_app.models import Cart, OrderItem



class OrderSaveView(View):
    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST)
        if form.is_valid() and Cart.objects.exists():
            order = form.save()
            for cart_item in Cart.objects.all():
                OrderItem.objects.create(
                    order=order,
                    product=cart_item.product,
                    quantity=cart_item.balance,
                )
            Cart.objects.all().delete()
            return redirect('product_list')
        return redirect('cart_list')



