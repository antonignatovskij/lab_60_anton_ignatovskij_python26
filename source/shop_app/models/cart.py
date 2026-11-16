from django.db import models


class Cart(models.Model):
    product = models.ForeignKey('shop_app.Product', null=False, blank=False, related_name='in_cart', on_delete=models.DO_NOTHING)
    balance = models.IntegerField(null=False, blank=False, default=0)

    class Meta:
        db_table = 'cart'
        verbose_name = 'Корзина'