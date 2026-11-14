from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=60, unique=True)
    description = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f'category:{self.pk} - {self.name}'

    class Meta:
        db_table = 'category'
        verbose_name = 'Категория'