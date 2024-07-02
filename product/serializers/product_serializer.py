from rest_framework import serializers

from product.models import Category, Products
from product.serializers.category_serializer import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=True, many=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), write_only=True, many=True)
    
    class Meta:
        model = Products
        fields = ['title', 'description', 'price', 'active', 'category', 'category_id']

    def create(self, validated_data):
        category_data = validated_data.pop('category_id')

        product = Products.objects.create(**validated_data)
        for category in category_data:
            product.category.add(category)
        
        return product