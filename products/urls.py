from django.urls import path
from .views import (
    CategoryCreateListView,
    CategoryUpdateListView,
    ProductListUpdateView,
    ProductListCreateView,
)

urlpatterns = [
    # List all products or create a new product
    # GET: /products/ - returns all products
    # POST: /products/ - creates a new product
    path("products/", ProductListCreateView.as_view(), name="product-list-create"),
    # Retrieve, update, or delete a specific product by its ID
    # GET: /products/<id>/ - returns product details
    # PUT: /products/<id>/ - updates product
    # DELETE: /products/<id>/ - deletes product
    path(
        "products/<int:pk>/",
        ProductListUpdateView.as_view(),
        name="product-list-update-delete",
    ),
    # List all categories or create a new category
    # GET: /category/ - returns all categories
    # POST: /category/ - creates a new category
    path("category/", CategoryCreateListView.as_view(), name="category-list-create"),
    # Retrieve, update, or delete a specific category by its ID
    # GET: /category/<id>/ - returns category details
    # PUT: /category/<id>/ - updates category
    # DELETE: /category/<id>/ - deletes category
    path(
        "category/<int:pk>/",
        CategoryUpdateListView.as_view(),
        name="category-list-update",
    ),
]
