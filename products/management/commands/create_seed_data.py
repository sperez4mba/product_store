from django.core.management.base import BaseCommand

from products.models import Category


class Command(BaseCommand):
    help = 'Create seed data for the product store api'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number-of-categories',
            type=int,
            default=1000,
            dest='number_of_categories'
        )

    def handle(self, *args, **options):
        Category.objects.all().delete()
        category_names = ["category_{}".format(str(i)) for i in range(options['number_of_categories'])]
        categories = [Category(name=name) for name in category_names]
        Category.objects.bulk_create(categories)
