import factory

from products.models import Category, Subcategory, Product


class RandomCategoryFactory(factory.Factory):
    class Meta:
        model = Category

    name = factory.Faker('name')


class RandomSubcategoryFactory(factory.Factory):
    class Meta:
        model = Subcategory

    name = factory.Faker('name')


class RandomProductFactory(factory.Factory):
    class Meta:
        model = Product

    name = factory.Faker('name')
