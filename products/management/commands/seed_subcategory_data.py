from django.core.management.base import BaseCommand

from products.models import Subcategory, Category


class Command(BaseCommand):
    help = 'Seed subcategory data, one subcategory per existing category'

    def handle(self, *args, **options):
        Subcategory.objects.all().delete()
        all_categories = Category.objects.all()
        number_of_existing_categories = all_categories.count()
        if number_of_existing_categories == 0:
            print('There are no existing categories')
            return
        subcategories = [Subcategory(name="sub{}".format(c.name), category=c) for c in all_categories]
        Subcategory.objects.bulk_create(subcategories)
