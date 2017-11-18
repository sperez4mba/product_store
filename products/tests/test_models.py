from unittest import TestCase

from products.models import Category, Subcategory, Product


class TestModels(TestCase):
    def test_(self):
        category_name_1 = 'Food Products'
        subcategory_name_1 = 'Rice and Legumes'
        subcategory_name_2 = 'Cooked Legumes'
        product_name = 'Cooked Pardina Lentils, Jar 570 G Runoff 400 G'

        category_1 = Category.objects.create(
            name=category_name_1
        )
        subcategory_1 = Subcategory.objects.create(
            name=subcategory_name_1,
            category=category_1
        )
        subcategory_2 = Subcategory.objects.create(
            name=subcategory_name_2,
            category=category_1
        )
        product = Product(
            name=product_name
        )
        product.subcategories.add(subcategory_1)
        product.subcategories.add(subcategory_2)
        import bpdb;bpdb.set_trace()
