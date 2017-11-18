from rest_framework import serializers

from products.models import Category, Subcategory, Product


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')


class SubcategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Subcategory
        fields = ('id', 'name', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')
