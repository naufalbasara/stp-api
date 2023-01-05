from rest_framework import serializers
from .models import User, Product, ProductBody, ProductDimension, ProductBattery, ProductPerformance, ProductComponent

class ProductBodySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductBody
        fields = '__all__'

class ProductDimensionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDimension
        fields = '__all__'

class ProductBatterySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductBattery
        fields = '__all__'

class ProductPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPerformance
        fields = '__all__'

class ProductComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductComponent
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'lastEditedBy', 'body_id', 'battery_id', 'dimension_id', 'performance_id', 'component_id', 'category', 'production_year', 'price')
        depth = 1


class CombinedSerializer(serializers.Serializer):
    product_body = ProductBodySerializer(many=True)
    product_dimension = ProductDimensionSerializer(many=True)
    product_battery = ProductBatterySerializer(many=True)
    product_performance = ProductPerformanceSerializer(many=True)
    product_component = ProductComponentSerializer(many=True)
    product = ProductSerializer(many=True)