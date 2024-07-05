from rest_framework import serializers
from productApp.models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('categoryId', 'name')

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Product
        fields = ('productId', 'name', 'description', 'price', 'category')
