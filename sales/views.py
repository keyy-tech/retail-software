from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import (
    SalesHeavySerializer,
    SalesLightSerializer,
    SalesItemHeavySerializer,
    SalesItemLightSerializer,
)
from .models import Sales, SaleItems

# Sales Views


# Sales Views (Heavy Serializer)
class SalesHeavyCreateList(APIView):
    """
    Handles listing all sales and creating a new sale with detailed (heavy) serializer.
    GET: Returns a list of all sales with detailed information.
    POST: Creates a new sale with the provided data.
    """

    def get(self, request):
        sales = Sales.objects.all()  # Fetch all sales
        serializer = SalesHeavySerializer(sales, many=True)  # Serialize sales list
        return Response(serializer.data)

    def post(self, request):
        serializer = SalesHeavySerializer(data=request.data)  # Deserialize input data
        if serializer.is_valid():
            serializer.save()  # Save new sale
            return Response(
                {"message": "Transaction successful", "content": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SalesHeavyViewUpdateDelete(APIView):
    """
    Handles retrieving, updating, partially updating, and deleting a single sale by its ID (heavy serializer).
    GET: Returns details of a specific sale.
    PUT: Updates a sale with the provided data.
    PATCH: Partially updates a sale.
    DELETE: Deletes the specified sale.
    """

    def get_object(self, pk):
        # Get sale by ID or raise 404 if not found
        try:
            return Sales.objects.get(pk=pk)
        except Sales.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        sales = self.get_object(pk)  # Get sale by ID
        serializer = SalesHeavySerializer(sales)  # Serialize sale
        return Response(serializer.data)

    def put(self, request, pk):
        sales = self.get_object(pk)
        serializer = SalesHeavySerializer(sales, data=request.data)  # Update sale
        if serializer.is_valid():
            serializer.save()  # Save updates
            return Response(
                {
                    "message": "Transaction updated successfully",
                    "content": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        sales = self.get_object(pk)
        serializer = SalesHeavySerializer(
            sales, data=request.data, partial=True
        )  # Partial update
        if serializer.is_valid():
            serializer.save()  # Save updates
            return Response(
                {
                    "message": "Transaction partially updated successfully",
                    "content": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        sales = self.get_object(pk)
        sales.delete()  # Delete sale
        return Response(
            {"message": "Transaction deleted successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )


# Sales Views (Light Serializer)
class SalesLightsCreateList(APIView):
    """
    Handles listing all sales and creating a new sale with basic (light) serializer.
    GET: Returns a list of all sales with basic information.
    POST: Creates a new sale with the provided data.
    """

    def get(self, request):
        sales = Sales.objects.all()  # Fetch all sales
        serializer = SalesLightSerializer(sales, many=True)  # Serialize sales list
        return Response(serializer.data)

    def post(self, request):
        serializer = SalesLightSerializer(data=request.data)  # Deserialize input data
        if serializer.is_valid():  # Check if data is valid
            serializer.save()  # Save new sale
            response = {
                "messages": "Transaction successful",
                "content": serializer.data,
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SalesLightViewUpdateDelete(APIView):
    """
    Handles retrieving, updating, partially updating, and deleting a single sale by its ID (light serializer).
    GET: Returns details of a specific sale.
    PUT: Updates a sale with the provided data.
    PATCH: Partially updates a sale.
    DELETE: Deletes the specified sale.
    """

    def get_object(self, pk):
        # Get sale by ID or raise 404 if not found
        try:
            return Sales.objects.get(pk=pk)
        except Sales.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        sales = self.get_object(pk)
        serializer = SalesLightSerializer(sales)
        return Response(serializer.data)

    def put(self, request, pk):
        sales = self.get_object(pk)
        serializer = SalesLightSerializer(sales, data=request.data)  # Update sale
        if serializer.is_valid():
            serializer.save()
            response = {
                "messages": "Transaction updated successfully",
                "content": serializer.data,
            }
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        sales = self.get_object(pk)
        serializer = SalesLightSerializer(
            sales, data=request.data, partial=True
        )  # Partial update
        if serializer.is_valid():
            serializer.save()
            response = {
                "messages": "Transaction partially updated successfully",
                "content": serializer.data,
            }
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        sales = self.get_object(pk)
        sales.delete()  # Delete sale
        return Response(
            {"message": "Transaction deleted successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )


# Sales Item Views (Heavy Serializer)
class SalesItemHeavyCreateList(APIView):
    """
    Handles listing all sale items and creating a new sale item with detailed (heavy) serializer.
    GET: Returns a list of all sale items with detailed information.
    POST: Creates a new sale item with the provided data.
    """

    def get(self, request):
        items = SaleItems.objects.all()  # Fetch all sale items
        serializer = SalesItemHeavySerializer(
            items, many=True
        )  # Serialize sale items list
        return Response(serializer.data)

    def post(self, request):
        serializer = SalesItemHeavySerializer(
            data=request.data
        )  # Deserialize input data
        if serializer.is_valid():  # Check if data is valid
            serializer.save()  # Save new sale item
            return Response(
                {"message": "Item added successfully", "content": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SalesItemHeavyViewUpdateDelete(APIView):
    """
    Handles retrieving, updating, partially updating, and deleting a single sale item by its ID (heavy serializer).
    GET: Returns details of a specific sale item.
    PUT: Updates a sale item with the provided data.
    PATCH: Partially updates a sale item.
    DELETE: Deletes the specified sale item.
    """

    def get_object(self, pk):
        # Get sale item by ID or raise 404 if not found
        try:
            return SaleItems.objects.get(pk=pk)
        except SaleItems.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        item = self.get_object(pk)
        serializer = SalesItemHeavySerializer(item)
        return Response(serializer.data)

    def put(self, request, pk):
        item = self.get_object(pk)
        serializer = SalesItemHeavySerializer(
            item, data=request.data
        )  # Update sale item
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Item updated successfully", "content": serializer.data},
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        item = self.get_object(pk)
        serializer = SalesItemHeavySerializer(
            item, data=request.data, partial=True
        )  # Partial update
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Item partially updated successfully",
                    "content": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        item = self.get_object(pk)
        item.delete()  # Delete sale item
        return Response(
            {"message": "Item deleted successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )


class SalesItemLightCreateList(APIView):
    """
    Handles listing all sale items and creating a new sale item with basic (light) serializer.
    GET: Returns a list of all sale items with basic information.
    POST: Creates a new sale item with the provided data.
    """

    def get(self, request):
        items = SaleItems.objects.all()  # Fetch all sale items
        serializer = SalesItemLightSerializer(
            items, many=True
        )  # Serialize sale items list
        return Response(serializer.data)

    def post(self, request):
        serializer = SalesItemLightSerializer(
            data=request.data
        )  # Deserialize input data
        if serializer.is_valid():
            serializer.save()  # Save new sale item
            return Response(
                {"message": "Item added successfully", "content": serializer.data},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SalesItemLightViewUpdateDelete(APIView):
    """
    Handles retrieving, updating, partially updating, and deleting a single sale item by its ID (light serializer).
    GET: Returns details of a specific sale item.
    PUT: Updates a sale item with the provided data.
    PATCH: Partially updates a sale item.
    DELETE: Deletes the specified sale item.
    """

    def get_object(self, pk):
        # Get sale item by ID or raise 404 if not found
        try:
            return SaleItems.objects.get(pk=pk)
        except SaleItems.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        item = self.get_object(pk)
        serializer = SalesItemLightSerializer(item)
        return Response(serializer.data)

    def put(self, request, pk):
        item = self.get_object(pk)
        serializer = SalesItemLightSerializer(
            item, data=request.data
        )  # Update sale item
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Item updated successfully", "content": serializer.data},
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        item = self.get_object(pk)
        serializer = SalesItemLightSerializer(
            item, data=request.data, partial=True
        )  # Partial update
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "Item partially updated successfully",
                    "content": serializer.data,
                },
                status=status.HTTP_200_OK,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        item = self.get_object(pk)
        item.delete()  # Delete sale item
        return Response(
            {"message": "Item deleted successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )
