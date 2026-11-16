from typing import Any

from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from shop_app.forms import ProductForm, SearchForm
from shop_app.models import Product


class ProductListView(ListView):
    template_name = 'products/index.html'
    context_object_name = 'products'
    model = Product
    paginate_by = 6
    paginate_orphans = 2
    ordering = ['category__name', 'name']

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.form
        context['title'] = self.title
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(balance__gte=1)
        self.title = 'Каталог товаров'
        if self.search_value:
            query = Q(name__icontains=self.search_value)
            self.title = f'Поиск товара по: {self.search_value}'
            if self.kwargs.get('category') is not None:
                self.title = f'Поиск товара в категории {self.kwargs.get('category')} по: {self.search_value}'
                query = Q(category__name=self.kwargs.get('category')) & Q(name__icontains=self.search_value)
            queryset = queryset.filter(query)
        if self.kwargs.get('category') is not None:
            self.title = f'Категория: {self.kwargs.get('category')}'
            query = Q(category__name=self.kwargs.get('category'))
            queryset = queryset.filter(query)
        return queryset


class ProductDetailView(DetailView):
    template_name = 'products/detail.html'
    model = Product
    queryset = Product.objects.filter(balance__gte=1)

class ProductCreateView(CreateView):
    template_name = 'products/create.html'
    model = Product
    form_class = ProductForm

    def get_success_url(self) -> str:
        return reverse('product_detail', kwargs={'pk': self.object.pk})

class ProductUpdateView(UpdateView):
    template_name = 'products/update.html'
    model = Product
    form_class = ProductForm

    def get_success_url(self) -> str:
        return reverse('product_detail', kwargs={'pk': self.object.pk})

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/delete.html'
    success_url = reverse_lazy('product_list')







