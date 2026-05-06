from rest_framework import serializers
from .models import CartItem
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()   # 👈 THIS IS THE KEY

    class Meta:
        model = CartItem
        fields = "__all__"