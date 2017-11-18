from rest_framework.generics import ListAPIView

from products.models import Category
from products.serializers import CategorySerializer


class CategoryList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
