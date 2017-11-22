from unittest import TestCase
from rest_framework import serializers

from products.api.v1.serializers import ProductSerializer
from products.models import Category, Subcategory, Product


class TestSerializers(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name='category_1')
        self.subcategory_name_1 = 'subcategory_1'
        self.subcategory_name_2 = 'subcategory_2'
        self.subcategory_1 = Subcategory.objects.create(
            name=self.subcategory_name_1,
            category=self.category
        )
        self.subcategory_2 = Subcategory.objects.create(
            name=self.subcategory_name_2,
            category=self.category
        )
        self.serializer = ProductSerializer()

    def tearDown(self):
        Category.objects.all().delete()
        Product.objects.all().delete()

    def test_exc_raised_when_creating_product_with_subcategories_empty(self):
        serialized_data = {'name': 'product_1', 'subcategories': []}

        try:
            self.serializer.create(serialized_data)
        except:
            self.assertRaises(serializers.ValidationError)

    def test_exc_raised_when_creating_product_but_no_existing_subcategories_provided(self):
        serialized_data = {'name': 'product_1', 'subcategories': [{'name': 'subcategory_0'}]}

        try:
            self.serializer.create(serialized_data)
        except:
            self.assertRaises(serializers.ValidationError)

    def test_creating_product_successfully_with_existing_subcategory(self):
        serialized_data = {'name': 'product_1', 'subcategories': [{'name': self.subcategory_name_1}]}

        self.serializer.create(serialized_data)

        all_products = Product.objects.all()
        self.assertEqual(1, len(all_products))
        self.assertEqual(1, len(all_products[0].subcategories.all()))
        self.assertEqual(
            self.subcategory_name_1,
            all_products[0].subcategories.all()[0].name
        )

    def test_updating_product_successfully_with_existing_categories(self):
        existing_product = Product.objects.create(name='product_1')
        existing_product.subcategories.add(self.subcategory_2)

        serialized_data = {'name': 'product_1', 'subcategories': [{'name': self.subcategory_name_2}, {'name': self.subcategory_name_1}]}

        self.serializer.update(existing_product, serialized_data)

        all_products = Product.objects.all()
        self.assertEqual(1, len(all_products))
        self.assertEqual(2, len(all_products[0].subcategories.all()))
        self.assertEqual(
            self.subcategory_name_1,
            all_products[0].subcategories.all()[0].name
        )
        self.assertEqual(
            self.subcategory_name_2,
            all_products[0].subcategories.all()[1].name
        )
