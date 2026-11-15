from typing import Any

from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView

from shop_app.forms import ProductForm
from shop_app.models import Product


class ProductsView(TemplateView):
    template_name = 'products/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context

class ProductDetailView(TemplateView):
    model = Product
    template_name = 'products/detail.html'

    def get_context_data(self, **kwargs):
        kwargs['product'] = get_object_or_404(Product, pk=kwargs['pk'])
        return super().get_context_data(**kwargs)


class ProductCreateView(TemplateView):
    model = Product
    template_name = 'products/create.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data()
        context['form'] = ProductForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ProductForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            product = Product.objects.create(**data)
            return redirect('product_detail', pk=product.pk)
        context = {'form': form}
        return self.render_to_response(context)

class ProductUpdateView(TemplateView):
    model = Product
    template_name = 'products/update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = get_object_or_404(Product, pk=context['pk'])
        context['form'] = ProductForm(initial={
            'name': product.name,
            'description': product.description,
            'category': product.category,
            'cost': product.cost,
            'image': product.image
        })
        return context

    def post(self, request, *args, **kwargs):
        form = ProductForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            product = get_object_or_404(Product, pk=kwargs['pk'])
            product.name = data['name']
            product.description = data['description']
            product.category = data['category']
            product.cost = data['cost']
            product.image = data['image']
            product.save()
            return redirect('product_detail', pk=product.pk)
        context = {'form': form}
        return self.render_to_response(context)

class ProductDeleteView(TemplateView):
    model = Product
    template_name = 'products/delete.html'

    def get_context_data(self, **kwargs):
        kwargs['object'] = get_object_or_404(Product, pk=kwargs['pk'])
        return super().get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=kwargs['pk'])
        product.delete()
        return redirect('product_list')







