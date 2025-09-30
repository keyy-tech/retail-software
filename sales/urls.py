from django.urls import path
from .views import (
    SalesHeavyCreateList,
    SalesHeavyViewUpdateDelete,
    SalesLightsCreateList,
    SalesLightViewUpdateDelete,
    SalesItemLightViewUpdateDelete,
    SalesItemLightCreateList,
    SalesItemHeavyViewUpdateDelete,
    SalesItemHeavyCreateList,
)

urlpatterns = [
    # Admin: List all sales or create a new sale (detailed info)
    # GET: /heavy/ - returns all sales (admin view)
    # POST: /heavy/ - creates a new sale (admin view)
    path("heavy/", SalesHeavyCreateList.as_view(), name="sales-heavy-list-create"),
    # Admin: Retrieve, update, or delete a sale by ID (detailed info)
    # GET: /heavy/<id>/ - returns sale details (admin view)
    # PUT: /heavy/<id>/ - updates sale (admin view)
    # PATCH: /heavy/<id>/ - partially updates sale (admin view)
    # DELETE: /heavy/<id>/ - deletes sale (admin view)
    path(
        "heavy/<int:pk>/",
        SalesHeavyViewUpdateDelete.as_view(),
        name="sales-heavy-detail",
    ),
    # Cashier: List all sales or create a new sale (basic info)
    # GET: /light/ - returns all sales (cashier view)
    # POST: /light/ - creates a new sale (cashier view)
    path("light/", SalesLightsCreateList.as_view(), name="sales-light-list-create"),
    # Cashier: Retrieve, update, or delete a sale by ID (basic info)
    # GET: /light/<id>/ - returns sale details (cashier view)
    # PUT: /light/<id>/ - updates sale (cashier view)
    # PATCH: /light/<id>/ - partially updates sale (cashier view)
    # DELETE: /light/<id>/ - deletes sale (cashier view)
    path(
        "light/<int:pk>/",
        SalesLightViewUpdateDelete.as_view(),
        name="sales-light-detail",
    ),
    # Cashier: List all sale items or create a new sale item (basic info)
    # GET: /item/light/ - returns all sale items (cashier view)
    # POST: /item/light/ - creates a new sale item (cashier view)
    path(
        "item/light/",
        SalesItemLightCreateList.as_view(),
        name="sales-item-light-list-create",
    ),
    # Cashier: Retrieve, update, or delete a sale item by ID (basic info)
    # GET: /item/light/<id>/ - returns sale item details (cashier view)
    # PUT: /item/light/<id>/ - updates sale item (cashier view)
    # PATCH: /item/light/<id>/ - partially updates sale item (cashier view)
    # DELETE: /item/light/<id>/ - deletes sale item (cashier view)
    path(
        "item/light/<int:pk>/",
        SalesItemLightViewUpdateDelete.as_view(),
        name="sales-item-light-detail",
    ),
    # Admin: List all sale items or create a new sale item (detailed info)
    # GET: /item/heavy/ - returns all sale items (admin view)
    # POST: /item/heavy/ - creates a new sale item (admin view)
    path(
        "item/heavy/",
        SalesItemHeavyCreateList.as_view(),
        name="sales-item-heavy-list-create",
    ),
    # Admin: Retrieve, update, or delete a sale item by ID (detailed info)
    # GET: /item/heavy/<id>/ - returns sale item details (admin view)
    # PUT: /item/heavy/<id>/ - updates sale item (admin view)
    # PATCH: /item/heavy/<id>/ - partially updates sale item (admin view)
    # DELETE: /item/heavy/<id>/ - deletes sale item (admin view)
    path(
        "item/heavy/<int:pk>/",
        SalesItemHeavyViewUpdateDelete.as_view(),
        name="sales-item-heavy-detail",
    ),
]
