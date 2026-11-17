from django.contrib import admin

from shop_app.models import Category, Product, Cart, OrderItem, Order

# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(OrderItem)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'mobile_phone',  'created_at']
    ordering = ('-created_at',)