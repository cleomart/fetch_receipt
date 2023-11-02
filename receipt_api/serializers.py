import uuid
import hashlib
from rest_framework import serializers
from .models import Receipt, Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['shortDescription', 'price']


class ReceiptSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)
    retailer = serializers.CharField(trim_whitespace=False)

    class Meta:
        model = Receipt
        fields = ['retailer', 'purchaseDate',
                  'purchaseTime', 'total', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop("items")
        print("validated_data ", validated_data)
        receipt = Receipt.objects.create(**validated_data)

        # Loop through the items data and create them if they do not exist yet in Item table
        for item in items_data:
            pk = self.generate_primary_key(item["shortDescription"] + item["price"])
            try:
                item_obj = Item.objects.get(id=pk)
            except Item.DoesNotExist as e:
                # If item does not exist, create the item object in the Item table
                item["id"] = pk
                item_obj = Item.objects.create(**item)

            # Add the item obj in the receipts list of items
            receipt.items.add(item_obj)
        return receipt

    def generate_primary_key(self, string):
        return uuid.UUID(hex=hashlib.md5(string.encode("UTF-8")).hexdigest())
