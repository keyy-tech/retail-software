from django.db import models


class Category(models.Model):
    """
    Represents a product category (e.g., Beverages, Snacks).
    Each product belongs to one category.
    """

    name = models.CharField(max_length=100)  # Name of the category

    def __str__(self):
        # Returns the category name for display in admin and logs
        return self.name


class Products(models.Model):
    """
    Represents a product in the inventory.
    Stores product details, pricing, stock, and category.
    """

    name = models.CharField(max_length=100)  # Name of the product
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)  # Price per unit
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE
    )  # Category this product belongs to
    sku = models.CharField(
        max_length=100, unique=True
    )  # Unique Stock Keeping Unit identifier
    stock_quantity = models.IntegerField()  # Current stock level
    created_at = models.DateTimeField(
        auto_now_add=True
    )  # Timestamp when product was created
    updated_at = models.DateTimeField(
        auto_now=True
    )  # Timestamp when product was last updated

    def __str__(self):
        # Returns the product name for display in admin and logs
        return self.name
