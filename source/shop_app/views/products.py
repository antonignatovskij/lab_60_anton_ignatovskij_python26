from django.views import View
from django.views.generic import TemplateView

from shop_app.models import Product


class ProductsView(TemplateView):
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context





