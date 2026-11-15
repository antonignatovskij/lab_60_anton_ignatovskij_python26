from django.shortcuts import redirect, get_object_or_404
from django.views.generic import TemplateView

from shop_app.models import Category
from shop_app.forms import CategoryForm

class CategoriesView(TemplateView):
    template_name = 'categories/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class CategoryCreateView(TemplateView):
    template_name = 'categories/create.html'

    def get_context_data(self, **kwargs):
        kwargs['form'] = CategoryForm()
        return super().get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        form = CategoryForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Category.objects.create(**data)
            return redirect('category_list')
        context = {'form': form}
        return self.render_to_response(context)

class CategoryUpdateView(TemplateView):
    template_name = 'categories/update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = get_object_or_404(Category, pk=context['pk'])
        context['form'] = CategoryForm(initial={
            'name': category.name,
            'description': category.description,
        })
        return context

    def post(self, request, *args, **kwargs):
        form = CategoryForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            category = get_object_or_404(Category, pk=kwargs['pk'])
            category.name = data['name']
            category.description = data['description']
            category.save()
            return redirect('category_list')
        context = {'form': form}
        return self.render_to_response(context)

class CategoryDeleteView(TemplateView):
    template_name = 'categories/delete.html'

    def get_context_data(self, **kwargs):
        kwargs['object'] = get_object_or_404(Category, pk=kwargs['pk'])
        return super().get_context_data(**kwargs)

    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Category, pk=kwargs['pk'])
        product.delete()
        return redirect('category_list')
