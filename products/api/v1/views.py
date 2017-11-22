from rest_framework.generics import ListAPIView, ListCreateAPIView, \
    UpdateAPIView

from products.models import Category, Product
from products.api.v1.serializers import CategorySerializer, \
    SubcategorySerializer, ProductSerializer


class CategoryList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductList(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdate(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
