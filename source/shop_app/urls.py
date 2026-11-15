from django.urls import path
from shop_app.views import (
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    product_list,

    CategoriesView,
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeleteView,
)

urlpatterns = [
    path('', product_list, name='product_list'),
    path('products/', product_list, name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/add/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<str:category>/', product_list, name='product_category_filter'),


    path('categories/', CategoriesView.as_view(), name='category_list'),
    path('categories/add', CategoryCreateView.as_view(), name='category_create'),
    path('categories/<int:pk>/edit/', CategoryUpdateView.as_view(), name='category_update'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
]