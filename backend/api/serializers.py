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

class ProductSerializer(serializers.ModelSerializer):
    body_id = ProductBodySerializer(many=True, required=False)
    dimension_id = ProductDimensionSerializer(many=True, required=False)
    battery_id = ProductBatterySerializer(many=True, required=False)
    performance_id = ProductPerformanceSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = [
            'name',
            'lastEditedBy',
            'body_id',
            'battery_id',
            'dimension_id',
            'performance_id',
            'category',
            'production_year',
            'price'
        ]
    
    def get_user(self, obj):
        return obj #dapetin user yang update atau modify product

    def create(self, validated_data):
        body_data = validated_data.pop('body_id')
        for data in body_data:
            body_obj = ProductBody.objects.create(**data)
        body_obj.save()
        
        dimension_data = validated_data.pop('dimension_id')
        for data in dimension_data:
            dimension_obj = ProductDimension.objects.create(**data)
        dimension_obj.save()

        battery_data = validated_data.pop('battery_id')
        for data in battery_data:
            battery_obj = ProductBattery.objects.create(**data)
        battery_obj.save()

        performance_data = validated_data.pop('performance_id')
        for data in performance_data:
            performance_obj = ProductPerformance.objects.create(**data)
        performance_obj.save()
        
        prod_obj = Product.objects.create(body_id = 1,
        dimension_id=1,
        battery_id = 1,
        performance_id = 1,
        **validated_data
        )

        print(battery_obj)
        return prod_obj