from rest_framework import serializers
from .models import Sales, SaleItems


class SalesItemLightSerializer(serializers.ModelSerializer):
    """
    Lightweight serializer for sale items.
    Used for cashier views where only basic item info is needed.
    Returns: id, product, and quantity.
    """

    class Meta:
        model = SaleItems
        fields = ["id", "product", "quantity"]


class SalesItemHeavySerializer(serializers.ModelSerializer):
    """
    Detailed serializer for sale items.
    Used for admin or business owner views where full item details are required.
    Adds product name and unit price for display.
    """

    product_name = serializers.CharField(source="product.name", read_only=True)
    unit_price = serializers.DecimalField(
        source="product.unit_price", max_digits=10, decimal_places=2
    )

    class Meta:
        model = SaleItems
        fields = "__all__"


class SalesLightSerializer(serializers.ModelSerializer):
    """
    Lightweight serializer for sales.
    Used for cashier views to show basic sale info and a list of items (with minimal details).
    """

    items = SalesItemLightSerializer(source="salesitems_set", many=True, read_only=True)

    class Meta:
        model = Sales
        fields = ["id", "date", "status", "payment_method", "items"]


class SalesHeavySerializer(serializers.ModelSerializer):
    """
    Detailed serializer for sales.
    Used for admin or business owner views to show all sale info and a list of items (with full details).
    """

    items = SalesItemHeavySerializer(source="salesitems_set", many=True, read_only=True)

    class Meta:
        model = Sales
        fields = ["id", "date", "status", "payment_method", "items"]
