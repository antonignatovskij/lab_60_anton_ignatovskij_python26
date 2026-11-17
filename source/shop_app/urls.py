from django.urls import path
from shop_app.views import (
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    ProductListView,

    CategoriesView,
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeleteView,

    CartProductView,
    CartListView,
    CartItemDeleteView,

    OrderSaveView,
)

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/add/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<str:category>/', ProductListView.as_view(), name='product_category_filter'),

    path('cart/product/<int:pk>/add', CartProductView.as_view(), name='cart_product_add'),
    path('cart/',CartListView.as_view(), name='cart_list'),
    path('cart/<int:pk>/delete', CartItemDeleteView.as_view(), name='cart_item_delete'),

    path('order/save', OrderSaveView.as_view(), name='order_save'),

    path('categories/', CategoriesView.as_view(), name='category_list'),
    path('categories/add', CategoryCreateView.as_view(), name='category_create'),
    path('categories/<int:pk>/edit/', CategoryUpdateView.as_view(), name='category_update'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
]