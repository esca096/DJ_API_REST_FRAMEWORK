from api.models import Product
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from api.api.serializers import ProductSerializer1, ProductSerializer2

# GET ==> Recuperation des données
# POST ==> Création des données
# PUT ==> Modification complète des données
# DELETE ==> Suppression des données
# PATCH ==> Modification partielle des données


@api_view(['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def product_api_view(request, pk=None, *args, **kwargs):
    if request.method == 'GET':
        #cette condition lier au serializer1 Recuperer l'id d'un elements dans le  model
        if pk is not None:
            product = get_object_or_404(Product, pk=pk)
            context = {'request':request}
            serializer = ProductSerializer1(product, context=context)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        #cette condition lier au serializer2 Recuperer tout les elements du models
        products = Product.objects.all()
        context = {'request':request}
        serializer = ProductSerializer1(products, many=True, context=context)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    #cette condition lier serializer1 permet de creer une nouvelle instance du models
    if request.method == 'POST':
        data = request.data
        name = data.get('name')
        serializer = ProductSerializer1(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #cette condition lier au serialize1 fait une Modification complète des données
    if request.method == 'PUT':
        if pk is None:
            return Response({'message':'You must provide a pk'}, status=status.HTTP_400_BAD_REQUEST)
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer1(product, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    #cette condition lier au serialize1 fait une suppression des données
    if request.method == 'DELETE':
        if pk is None:
            return Response({'message':'you must provide a pk'}, status=status.HTTP_400_BAD_REQUEST)
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return Response({'message':'product deleted'}, status=status.HTTP_200_OK)
    
    #cette condition lier au serialize1 fait une Modification partielle des données
    if request.method == 'PATCH':
        if pk is None:
            return Response({'message':'you must provide a pk'}, status=status.HTTP_400_BAD_REQUEST)
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer1(product, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

