
from rest_framework import fields, serializers

from products.models import BasketItem, Product, ProductCategory


class ProductsSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', queryset=ProductCategory.objects.all())

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'quantity', 'image', 'category')


class BasketItemSerializer(serializers.ModelSerializer):
    product = ProductsSerializer()
    sum = fields.FloatField(required=False)  # Вызов функции sum из модели BasketItem
    total_sum = fields.SerializerMethodField()
    total_quantity = fields.SerializerMethodField()

    class Meta:
        model = BasketItem
        fields = ('id', 'product', 'quantity', 'sum', 'total_sum', 'total_quantity', 'created_timestamp')
        read_only_fields = ('created_timestamp',)

    def get_total_sum(self, obj):
        return BasketItem.objects.filter(user_id=obj.user.id).total_sum()

    def get_total_quantity(self, obj):
        return BasketItem.objects.filter(user_id=obj.user.id).total_quantity()
