from api.api.serializers import ProductSerializer1
from api.models import Product
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response
from rest_framework import status


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer1
    queryset = Product.objects.all()