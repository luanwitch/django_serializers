from rest_framework import serializers
from .models import Order
from products.models import Product
from products.serializers import ProductSerializer

class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)  # retorno detalhado do produto
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        source='product',
        write_only=True
    )

    class Meta:
        model = Order
        fields = ['id', 'product', 'product_id', 'quantity', 'status', 'created_at']
        read_only_fields = ['id', 'created_at']
