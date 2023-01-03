import json
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer

#get list and create products
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save()
        # if serializer.is_valid():
            # return Response({"Status": 201, "Message": "Product object have been created"})
        # return Response({"Status": 400, "Message": "Failed to upload data"})

#get detail, update, and destroy product
class ProductDetailUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if serializer.is_valid():
            return Response({"Status": 204, })
        return Response({"Status": 400, "Message": "Failed to update data"})

    def perform_destroy(self, instance):
        super().perform_destroy(instance)
        return Response({"Status": 204, "Message": "Object deleted"})