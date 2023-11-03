import uuid
import hashlib

from .validators import *
from .models import Receipt, Item
from rest_framework import serializers

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['shortDescription', 'price', 'id']

    def validate(self, data):
        """ Initial validation of the input data"""
        check_unknown_fields(self)
        price_validator_serializer(self)
        return data


class ReceiptSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)
    retailer = serializers.CharField(trim_whitespace=False)

    class Meta:
        model = Receipt
        fields = ['retailer', 'purchaseDate',
                  'purchaseTime', 'total', 'items']

    def validate(self, data):
        """ Initial validation of the input data"""
        check_unknown_fields(self)
        check_items_min_count(self)
        check_date_and_time_format(self)
        total_validator_serializer(self)
        total_price_validator(self)
        return data

    def create(self, validated_data):
        """ Handle the creation of Receipt and Item objects """
        validated_data.pop("items")
        # Use initial data so Serializer will be able to validate them
        items_data = self.initial_data.pop("items")
        receipt = Receipt.objects.create(**validated_data)

        # Loop through the items data and create them if they do not exist yet in Item table
        for item in items_data:
            pk = self.generate_primary_key(item["shortDescription"] + item["price"])
            item_serializer = ItemSerializer(data=item)
            if item_serializer.is_valid(raise_exception=True):
                try:
                    item_obj = Item.objects.get(id=pk)
                except Item.DoesNotExist as e:
                    # If item does not exist, create the item object in the Item table
                    item_obj = item_serializer.save()

            # Add the item obj in the receipts list of items
            receipt.items.add(item_obj)
        return receipt

    def generate_primary_key(self, string):
        """ Generate UUID as the primary key for item """
        return uuid.UUID(hex=hashlib.md5(string.encode("UTF-8")).hexdigest())

