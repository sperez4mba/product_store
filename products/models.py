from django.db import models


class BaseResource(models.Model):
    name = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Category(BaseResource):

    class Meta:
        verbose_name_plural = 'categories'


class Subcategory(BaseResource):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='subcategories'
    )

    class Meta:
        verbose_name_plural = 'subcategories'


class Product(BaseResource):
    subcategories = models.ManyToManyField(Subcategory)
