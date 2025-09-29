from django.db import models

from products.models import Products


# Create your models here.
class Sales(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    status = models.CharField(choices=STATUS_CHOICES,max_length=20)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Cash'),
        ('mobile payment', 'Mobile Payment'),
    ]
    payment_method = models.CharField(choices=PAYMENT_METHOD_CHOICES,max_length=20)

    def __str__(self):
        return str(self.date)

    class Meta:
        ordering = ['-date']


class SaleItems(models.Model):
    sales = models.ForeignKey(Sales, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self,*args,**kwargs):
        self.subtotal = self.quantity * self.product.unit_price
        super().save(*args,**kwargs)


    def __str__(self):
        return str(self.sales.date) +  str(self.product.name) + str(self.subtotal)
