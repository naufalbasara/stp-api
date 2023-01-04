import json
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from .models import Product
from .serializers import ProductBodySerializer, ProductDimensionSerializer, ProductBatterySerializer, ProductPerformanceSerializer, ProductComponentSerializer, ProductSerializer, CombinedSerializer

#get list and create products
class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

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

@api_view(['POST'])
def alt_product(request, pk=None, *args, **kwargs):
    method = request.method
    print(request.data)
    if method == 'POST':
        #get data of product body
        body_data = {}
        body_data['product_class'] = request.data['product_class']
        body_data['style'] = request.data['style']
        body_data['layout'] = request.data['layout']
        body_data['frame'] = request.data['frame']
        print(body_data)

        body_serializer = ProductBodySerializer(data=body_data)

        #get data of product battery
        battery_data = {}
        battery_data['battery_capacity'] = request.data['battery_capacity']
        battery_data['charge_port'] = request.data['charge_port']
        battery_data['port_location'] = request.data['port_location']
        battery_data['voltage'] = request.data['voltage']
        battery_data['charging_time'] = request.data['charging_time']
        print(battery_data)

        battery_serializer = ProductBatterySerializer(data=battery_data)
        if battery_serializer.is_valid(raise_exception=True):
            battery_serializer.save()

        #get data of product dimension
        dimension_data = {}
        dimension_data['length'] = request.data['length']
        dimension_data['width'] = request.data['width']
        dimension_data['height'] = request.data['height']
        dimension_data['wheelbase'] = request.data['wheelbase']
        dimension_data['weight'] = request.data['weight']
        print(dimension_data)

        dimension_serializer = ProductDimensionSerializer(data=dimension_data)

        #get data of product performance
        performance_data = {}
        performance_data['top_speed'] = request.data['top_speed']
        performance_data['electric_range'] = request.data['electric_range']
        performance_data['power'] = request.data['power']
        performance_data['torque'] = request.data['torque']
        performance_data['drivetrain'] = request.data['drivetrain']
        print(performance_data)

        performance_serializer = ProductPerformanceSerializer(data=performance_data)

        #get data of product component
        component_data = {}
        component_data['rim'] = request.data['rim']
        component_data['front_tire'] = request.data['front_tire']
        component_data['rear_tire'] = request.data['rear_tire']
        component_data['front_suspension'] = request.data['front_suspension']
        component_data['rear_suspension'] = request.data['rear_suspension']
        component_data['front_brake'] = request.data['front_brake']
        component_data['rear_brake'] = request.data['rear_brake']
        print(component_data)

        component_serializer = ProductComponentSerializer(data=component_data)
        print("serializer checkpoint")
        serializers = [body_serializer, battery_serializer, dimension_serializer, performance_serializer, component_serializer]
        ids = {}
        count = 1
        for serializer in serializers:
            serializer.is_valid(raise_exception=True)
            serializer.save()
            ids[f'id_{count}'] = serializer.data['id']
            count+=1

        print('save serializer check')
        product_data = {}
        product_data['name'] = request.data['name']
        product_data['body_id'] = ids['id_1']
        product_data['battery_id'] = ids['id_2']
        product_data['dimension_id'] = ids['id_3']
        product_data['performance_id'] = ids['id_4']
        product_data['component_id'] = ids['id_5']
        product_data['category'] = request.data['category']
        product_data['production_year'] = request.data['production_year']
        product_data['price'] = request.data['price']
        
        product_serializer = ProductSerializer(data=product_data)

        if product_serializer.is_valid(raise_exception=True):
            product_serializer.save()
            return Response({"Status": 201, "Message": f"Product {product_data['name']} object have been created!"})
        return Response({"Status": 400, "Message": "Failed to create data due to bad request has been sent."})

