from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    category = models.ForeignKey('shop_app.Category', related_name='products', on_delete=models.CASCADE, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.CharField(null=False, blank=False)

    def __str__(self):
        return f'product:{self.pk} - {self.name}'

    class Meta:
        db_table = 'product'
        verbose_name = 'Товар'