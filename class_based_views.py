from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ItemsSerializer
from .models import Items

class ItemList(APIView):
    def get(self, request):
        items = Items.objects.all()
        serializer = ItemsSerializer(items, many=True)
        return Response({"items": serializer.data})

    def post(self, request):
        serializer = ItemsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemDetail(APIView):
    def get(self, request, id):
        try:
            item = Items.objects.get(pk=id)
        except Items.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ItemsSerializer(item)
        return Response(serializer.data)

    def put(self, request, id):
        try:
            item = Items.objects.get(pk=id)
        except Items.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ItemsSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            item = Items.objects.get(pk=id)
        except Items.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
