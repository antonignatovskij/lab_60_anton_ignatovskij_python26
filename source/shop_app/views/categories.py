from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from shop_app.models import Category
from shop_app.forms import CategoryForm

class CategoriesView(ListView):
    template_name = 'categories/index.html'
    model = Category
    context_object_name = 'categories'

class CategoryCreateView(CreateView):
    template_name = 'categories/create.html'
    form_class = CategoryForm
    model = Category
    success_url = reverse_lazy('category_list')

class CategoryUpdateView(UpdateView):
    template_name = 'categories/update.html'
    form_class = CategoryForm
    model = Category
    success_url = reverse_lazy('category_list')

class CategoryDeleteView(DeleteView):
    template_name = 'categories/delete.html'
    model = Category
    success_url = reverse_lazy('category_list')
