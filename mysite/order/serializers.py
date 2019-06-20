from rest_framework import serializers
from users.serializers import UserSerializer
from order.models import Order, OrderItem
from shop.serializers import ProductSerializer


class OrderSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    owned_by = UserSerializer(read_only=True)
    address = serializers.CharField(required=True)
    postal_code = serializers.CharField(required=True)
    city = serializers.CharField(required=True)

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        return Order.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.address = validated_data.get('address', instance.address)
        instance.postal_code = validated_data.get('postal_code', instance.postal_code)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance


class OrderItemSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    order = OrderSerializer(read_only=True)
    product = ProductSerializer(required=True)
    quantity = serializers.IntegerField()

    def create(self, validated_data):
        return OrderItem.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.quantity = validated_data.get('quantity', instance.quanity)
        instance.save()
        return instance
