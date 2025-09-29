from django.urls import path
from .views import CategoryCreateListView, CategoryUpdateListView,ProductListUpdateView, ProductListCreateView

urlpatterns = [
    path("products/",ProductListCreateView.as_view(),name="product-list-create"),
    path("products/<int:pk>/",ProductListUpdateView.as_view(),name="product-list-update-delete"),
    path("category/",CategoryCreateListView.as_view(),name="category-list-create"),
    path("category/<int:pk>/",CategoryUpdateListView.as_view(),name="category-list-update"),
]