from django.db import models
from products.models import Products


class Sales(models.Model):
    """
    Represents a single sale transaction.
    Stores the date, status, total amount, and payment method for the sale.
    """

    date = models.DateTimeField(
        auto_now_add=True
    )  # Date and time when the sale was created
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    ]
    status = models.CharField(
        choices=STATUS_CHOICES, max_length=20
    )  # Current status of the sale
    total_amount = models.DecimalField(
        max_digits=10, decimal_places=2, default=0
    )  # Total amount for the sale
    PAYMENT_METHOD_CHOICES = [
        ("cash", "Cash"),
        ("mobile payment", "Mobile Payment"),
    ]
    payment_method = models.CharField(
        choices=PAYMENT_METHOD_CHOICES, max_length=20
    )  # How the sale was paid

    def __str__(self):
        # String representation for easy identification in admin and logs
        return f"Sale {self.id} - {self.date} - {self.total_amount}"

    class Meta:
        ordering = ["-date"]  # Show most recent sales first

    def update_total(self):
        """
        Recalculate and update the total amount for this sale
        by summing the subtotals of all related SaleItems.
        """
        total = sum(item.subtotal for item in self.saleitems_set.all())
        self.total_amount = total
        self.save(update_fields=["total_amount"])


class SaleItems(models.Model):
    """
    Represents an individual item within a sale.
    Links to a product, stores quantity, and calculates subtotal.
    """

    sales = models.ForeignKey(
        Sales, on_delete=models.CASCADE
    )  # The sale this item belongs to
    product = models.ForeignKey(
        Products, on_delete=models.CASCADE
    )  # The product being sold
    quantity = models.DecimalField(
        max_digits=10, decimal_places=2
    )  # Quantity of the product sold
    subtotal = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True
    )  # Subtotal for this item

    def save(self, *args, **kwargs):
        """
        Calculate the subtotal before saving.
        After saving, update the parent sale's total amount.
        """
        self.subtotal = self.quantity * self.product.unit_price
        super().save(*args, **kwargs)
        self.sales.update_total()

    def delete(self, *args, **kwargs):
        """
        When an item is deleted, update the parent sale's total amount.
        """
        super().delete(*args, **kwargs)
        self.sales.update_total()

    def __str__(self):
        # String representation for easy identification in admin and logs
        return f"{self.product.name} x {self.quantity} = {self.subtotal}"
