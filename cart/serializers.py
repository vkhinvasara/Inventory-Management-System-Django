from rest_framework import serializers
from .models import Cart
from inventory.models import Item

class ItemSerializer(serializers.Serializer):
    item_id = serializers.CharField(max_length=200)
    name = serializers.CharField(max_length=200)
    price = serializers.FloatField()
    quantity = serializers.IntegerField()

    def create(self, validated_data):
        try:
            return Item.objects.get(item_id=validated_data['item_id'])
        except Item.DoesNotExist:
            raise serializers.ValidationError("The item does not exist")

class CartSerializer(serializers.Serializer):
    customer_id = serializers.CharField(max_length=200)
    items = ItemSerializer(many=True)

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        cart = Cart(**validated_data)
        for item_data in items_data:
            Item.objects.create(cart=cart, **item_data)
        return cart