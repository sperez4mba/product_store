from rest_framework import serializers

from products.models import Category, Subcategory, Product


class SubcategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subcategory
        fields = ('id', 'name', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')


class SubcategorySerializer(serializers.Serializer):
    name = serializers.CharField()


class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubcategoryListSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ('id', 'name', 'created_at', 'updated_at', 'subcategories')
        read_only_fields = ('created_at', 'updated_at', 'subcategories')


class ProductSerializer(serializers.ModelSerializer):
    subcategories = SubcategorySerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'created_at', 'updated_at', 'subcategories')
        read_only_fields = ('created_at', 'updated_at')

    def create(self, validated_data):
        subcategory_data = validated_data.pop('subcategories')
        if not subcategory_data:
            raise serializers.ValidationError(
                'At least one subcategory name must be provided.'
            )
        product_subcategories = []
        for data in subcategory_data:
            try:
                subcategory = Subcategory.objects.get(name=data['name'])
                if subcategory not in product_subcategories:
                    product_subcategories.append(subcategory)
            except Exception as e:
                print("Subcategory with name {} doesn't "
                      "exist".format(data['name']))
                continue
        if not product_subcategories:
            raise serializers.ValidationError(
                'None of the subcategories provided exists, at least one existing subcategory must be provided.'
            )
        product = Product.objects.create(**validated_data)
        [product.subcategories.add(so) for so in product_subcategories]
        return product

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        subcategory_data = validated_data.pop('subcategories')
        product_subcategories = []
        for data in subcategory_data:
            try:
                subcategory = Subcategory.objects.get(name=data['name'])
                if subcategory not in product_subcategories:
                    product_subcategories.append(subcategory)
            except Exception as e:
                print("Subcategory with name {} doesn't exist".format(
                    data['name']
                ))
                continue
        if product_subcategories:
            instance.subcategories = []
            [instance.subcategories.add(so) for so in product_subcategories]
        else:
            print("Subcategory with name {} doesn't exist".format(
                data['name']
                ))
        instance.save()
        return instance
