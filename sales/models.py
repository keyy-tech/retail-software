from django.db import models
from products.models import Products


class Sales(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    status = models.CharField(choices=STATUS_CHOICES, max_length=20)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Cash'),
        ('mobile payment', 'Mobile Payment'),
    ]
    payment_method = models.CharField(choices=PAYMENT_METHOD_CHOICES, max_length=20)

    def __str__(self):
        return f"Sale {self.id} - {self.date} - {self.total_amount}"

    class Meta:
        ordering = ['-date']

    def update_total(self):
        """Recalculate and update the total amount from related SaleItems"""
        total = sum(item.subtotal for item in self.saleitems_set.all())
        self.total_amount = total
        self.save(update_fields=['total_amount'])


class SaleItems(models.Model):
    sales = models.ForeignKey(Sales, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        # calculate subtotal before saving
        self.subtotal = self.quantity * self.product.unit_price
        super().save(*args, **kwargs)

        # update parent sale total
        self.sales.update_total()

    def delete(self, *args, **kwargs):
        # when an item is deleted, recalc parent sale total
        super().delete(*args, **kwargs)
        self.sales.update_total()

    def __str__(self):
        return f"{self.product.name} x {self.quantity} = {self.subtotal}"
