from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Products, Category
from .serializers import ProductSerializer, CategorySerializer


# Create your views here.
# Products Views
class ProductListCreateView(APIView):
    def get(self, request):
        products = Products.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "Product created successfully",
                "product": serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductListUpdateView(APIView):
    def get_object(self,pk):
        try:
            return Products.objects.get(pk=pk)
        except Products.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "Product updated successfully",
                "product": serializer.data
            }
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()
        response = {
            "message": "Product deleted successfully",
        }
        return Response(response, status=status.HTTP_200_OK)

# Category Views
class CategoryCreateListView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "Category created successfully",
                "categories": serializer.data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryUpdateListView(APIView):

   def get_object(self,pk):
       try:
           return Category.objects.get(pk=pk)
       except Category.DoesNotExist:
           raise Http404

   def get(self, request, pk):
       category = self.get_object(pk)
       serializer = CategorySerializer(category)
       return Response(serializer.data)

   def put(self, request, pk):
       category = self.get_object(pk)
       serializer = CategorySerializer(category, data=request.data)
       if serializer.is_valid():
           serializer.save()
           response = {
               "message": "Category updated successfully",
               "category": serializer.data
           }
           return Response(response, status=status.HTTP_200_OK)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   def delete(self, request, pk):
       category = self.get_object(pk)
       category.delete()
       response = {
           'message': 'Category deleted successfully',
       }
       return Response(response, status=status.HTTP_200_OK)
