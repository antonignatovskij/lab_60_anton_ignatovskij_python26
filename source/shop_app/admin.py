from django.contrib import admin

from shop_app.models import Category, Product, Cart, OrderItem

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(OrderItem)