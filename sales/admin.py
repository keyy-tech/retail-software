from django.contrib import admin

from sales.models import Sales, SaleItems


# Register your models here.
@admin.register(Sales)
class SalesAdmin(admin.ModelAdmin):
    pass


@admin.register(SaleItems)
class SaleItemsAdmin(admin.ModelAdmin):
    pass
