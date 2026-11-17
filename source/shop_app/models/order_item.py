from django.db import models


class OrderItem(models.Model):
    order = models.ForeignKey('shop_app.Order', on_delete=models.CASCADE)
    product = models.ForeignKey('shop_app.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)

    class Meta:
        db_table = 'order_item'
        verbose_name = 'Промежуточная таблица между заказом и товаром'