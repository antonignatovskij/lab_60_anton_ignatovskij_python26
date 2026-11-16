from django.http import Http404
from django.shortcuts import redirect
from django.views.generic import View, ListView
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


class CartListView(ListView):
    template_name = 'cart/index.html'
    model = Cart
    context_object_name = 'cart'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['cart'] = Cart.objects.all()
        for item in context['cart']:
            item.total_price = item.balance * item.product.cost
        context['total_sum'] = sum(item.total_price for item in context['cart'])
        return context

class CartItemDeleteView(View):
    def post(self, request, *args, **kwargs):
        product = Product.objects.get(id=kwargs['pk'])
        cart_item = Cart.objects.filter(product=product).first()
        if cart_item is None:
            raise Http404
        action = request.POST.get('action')
        if action == 'delete_all':
            cart_item.delete()
        elif action == 'delete_one':
            if cart_item.balance <= 1:
                cart_item.delete()
            else:
                cart_item.balance -= 1
                cart_item.save()
        return redirect('cart_list')

