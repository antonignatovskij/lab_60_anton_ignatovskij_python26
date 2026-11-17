from django.db import models


class Order(models.Model):
    full_name = models.CharField(null=False, blank=False, max_length=200)
    mobile_phone = models.CharField(null=False, blank=False, max_length=200)
    address = models.CharField(null=False, blank=False, max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    products = models.ManyToManyField('shop_app.Product', through='OrderItem', related_name='orders')

    class Meta:
        db_table = 'order'
        verbose_name = 'Заказ'