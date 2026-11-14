from django.urls import path
from shop_app.views import ProductsView
urlpatterns = [
    path('', ProductsView.as_view(), name='products_list'),
]