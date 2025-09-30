from rest_framework import serializers
from .models import Products, Category


class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for the Products model.
    Converts Product instances to and from JSON for API requests and responses.
    Includes all fields of the Products model.
    """

    class Meta:
        model = Products
        fields = "__all__"  # Serialize all fields in the Products model


class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer for the Category model.
    Converts Category instances to and from JSON for API requests and responses.
    Includes all fields of the Category model.
    """

    class Meta:
        model = Category
        fields = "__all__"  # Serialize all fields in the Category model
