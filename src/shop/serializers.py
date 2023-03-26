from rest_framework import serializers

from .models import Product, Size


class SizeSerializer(serializers.ModelSerializer):
    price = serializers.IntegerField()

    class Meta:
        model = Size
        fields = ('title', 'price')


class ProductSerializer(serializers.ModelSerializer):
    size = SizeSerializer(source='sizes', many=True, read_only=True)
    brand_name = serializers.CharField(source='brand.name')
    price = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('title', 'sku', 'brand_name', 'price', 'size')

    @staticmethod
    def get_price(instance):
        return min(size.price for size in instance.sizes.all())
