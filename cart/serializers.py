from rest_framework import serializers
from .models import Cart
from inventory.models import Item

class ItemSerializer(serializers.Serializer):
    item_id = serializers.IntegerField()
    quantity = serializers.IntegerField()

class CartSerializer(serializers.Serializer):
    customer_id = serializers.IntegerField()
    items = ItemSerializer(many=True)

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        cart = Cart(**validated_data)
        for item_data in items_data:
            Item.objects[item_data['item_id']] = Item(**item_data)
        return cart

    def update(self, instance, validated_data):
        instance.customer_id = validated_data.get('customer_id', instance.customer_id)
        items_data = validated_data.pop('items')
        for item_data in items_data:
            Item.objects[item_data['item_id']] = Item(**item_data)
        return instance