from model_mommy.recipe import Recipe

from products.models import Category


category = Recipe(
    Category,
    name = 'cereals'
)
