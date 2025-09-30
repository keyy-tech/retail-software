from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Products, Category
from .serializers import ProductSerializer, CategorySerializer


# Product Views
class ProductListCreateView(APIView):
    """
    Handles listing all products and creating a new product.
    GET: Returns a list of all products.
    POST: Creates a new product with the provided data.
    """

    def get(self, request):
        products = Products.objects.all()  # Fetch all products
        serializer = ProductSerializer(products, many=True)  # Serialize product list
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)  # Deserialize input data
        if serializer.is_valid():
            serializer.save()  # Save new product
            response = {
                "message": "Product created successfully",
                "product": serializer.data,
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductListUpdateView(APIView):
    """
    Handles retrieving, updating, and deleting a single product by its ID.
    GET: Returns details of a specific product.
    PUT: Updates a product with the provided data.
    DELETE: Deletes the specified product.
    """

    def get_object(self, pk):
        # Helper method to get a product or raise 404 if not found
        try:
            return Products.objects.get(pk=pk)
        except Products.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        product = self.get_object(pk)  # Get product by ID
        serializer = ProductSerializer(product)  # Serialize product
        return Response(serializer.data)

    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(
            product, data=request.data
        )  # Deserialize and update
        if serializer.is_valid():
            serializer.save()  # Save updates
            response = {
                "message": "Product updated successfully",
                "product": serializer.data,
            }
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(
            product, data=request.data, partial=True
        )  # Deserialize and update partially
        if serializer.is_valid():
            serializer.save()  # Save updates
            response = {
                "message": "Product partially updated successfully",
                "product": serializer.data,
            }
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()  # Delete product
        response = {
            "message": "Product deleted successfully",
        }
        return Response(response, status=status.HTTP_200_OK)


# Category Views


class CategoryCreateListView(APIView):
    """
    Handles listing all categories and creating a new category.
    GET: Returns a list of all categories.
    POST: Creates a new category with the provided data.
    """

    def get(self, request):
        categories = Category.objects.all()  # Fetch all categories
        serializer = CategorySerializer(
            categories, many=True
        )  # Serialize category list
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)  # Deserialize input data
        if serializer.is_valid():
            serializer.save()  # Save new category
            response = {
                "message": "Category created successfully",
                "categories": serializer.data,
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryUpdateListView(APIView):
    """
    Handles retrieving, updating, and deleting a single category by its ID.
    GET: Returns details of a specific category.
    PUT: Updates a category with the provided data.
    DELETE: Deletes the specified category.
    """

    def get_object(self, pk):
        # Helper method to get a category or raise 404 if not found
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        category = self.get_object(pk)  # Get category by ID
        serializer = CategorySerializer(category)  # Serialize category
        return Response(serializer.data)

    def put(self, request, pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(
            category, data=request.data
        )  # Deserialize and update
        if serializer.is_valid():
            serializer.save()  # Save updates
            response = {
                "message": "Category updated successfully",
                "category": serializer.data,
            }
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        category = self.get_object(pk)
        category.delete()  # Delete category
        response = {
            "message": "Category deleted successfully",
        }
        return Response(response, status=status.HTTP_200_OK)
