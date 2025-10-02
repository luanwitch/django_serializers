from rest_framework import serializers
from .models import Product
from categories.models import Category
from categories.serializers import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True) 
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True
    )

    class Meta:
        model = Product
        fields = ['id', 'name', 'stock', 'price', 'category', 'category_id']
        read_only_fields = ['id']
