from django.shortcuts import redirect
from django.views.generic import View
from shop_app.models import Cart, Product
from shop_app.forms import CartForm


class CartProductView(View):

    def post(self, request, *args, **kwargs):
        product = Product.objects.get(id=kwargs['pk'])
        cart = Cart.objects.filter(product=product).first()
        from_page = request.POST.get('from_page')
        if cart is not None:
            form = CartForm(instance=cart, data=request.POST)
            if form.is_valid():
                cart.save()
                return redirect(from_page)
            return redirect(from_page)
        form = CartForm(request.POST)
        form.instance.product = product
        if form.is_valid():
            form.save()
        from_page = request.POST.get('from_page')
        return redirect(from_page)
