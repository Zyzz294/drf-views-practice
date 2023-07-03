from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin

from .models import Items
from .serializers import ItemsSerializer

class ItemListCreateAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):

    queryset = Items.objects.all()
    serializer_class = ItemsSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) 
