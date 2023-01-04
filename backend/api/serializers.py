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
    # body_serializer = ProductBodySerializer(many=True)
    # dimension_serializer = ProductDimensionSerializer(many=True)
    # battery_serializer = ProductBatterySerializer(many=True)
    # performance_serializer = ProductPerformanceSerializer(many=True)
    # component_serializer = ProductComponentSerializer(many=True)

    class Meta:
        model = Product
        fields = ('name', 'lastEditedBy', 'body_id', 'battery_id', 'dimension_id', 'performance_id', 'component_id', 'category', 'production_year', 'price')
        # fields = '__all__'
        # read_only_fields = ('lastEditedBy', 'body_id', 'battery_id', 'dimension_id', 'performance_id', 'component_id')
        depth = 1

        # body_serializer = ProductBodySerializer()
        # print(body_serializer)
        # if body_serializer.is_valid(raise_exception=True):
        #     body_data = {}
        #     body_data['product_class'] = body_serializer.validated_data.get('product_class')
        #     body_data['style'] = body_serializer.validated_data.get('style')
        #     body_data['layout'] = body_serializer.validated_data.get('layout')
        #     body_data['frame'] = body_serializer.validated_data.get('frame')

        #     body_serializer.save()

        # battery_data = {}
        # battery_data['battery_capacity'] = validated_data.get('battery_capacity')
        # battery_data['charge_port'] = validated_data.get('charge_port')
        # battery_data['port_location'] = validated_data.get('port_location')
        # battery_data['voltage'] = validated_data.get('voltage')
        # battery_data['charging_time'] = validated_data.get('charging_time')

        # battery_serializer = ProductBatterySerializer(data=battery_data)
        # if battery_serializer.is_valid(raise_exception=True):
        #     battery_serializer.save()

        # dimension_data = {}
        # dimension_data['length'] = validated_data.get('length')
        # dimension_data['width'] = validated_data.get('width')
        # dimension_data['height'] = validated_data.get('height')
        # dimension_data['wheelbase'] = validated_data.get('wheelbase')
        # dimension_data['weight'] = validated_data.get('weight')

        # dimension_serializer = ProductDimensionSerializer(data=dimension_data)
        # if dimension_serializer.is_valid(raise_exception=True):
        #     dimension_serializer.save()

        # performance_data = {}
        # performance_data['top_speed'] = validated_data.get('top_speed')
        # performance_data['electric_range'] = validated_data.get('electric_range')
        # performance_data['power'] = validated_data.get('power')
        # performance_data['torque'] = validated_data.get('torque')
        # performance_data['drivetrain'] = validated_data.get('drivetrain')

        # performance_serializer = ProductPerformanceSerializer(data=performance_data)
        # if performance_serializer.is_valid(raise_exception=True):
        #     performance_serializer.save()

        # component_data = {}
        # component_data['rim'] = validated_data.get('rim')
        # component_data['front_tire'] = validated_data.get('front_tire')
        # component_data['rear_tire'] = validated_data.get('rear_tire')
        # component_data['front_suspension'] = validated_data.get('front_suspension')
        # component_data['rear_suspension'] = validated_data.get('rear_suspension')
        # component_data['front_brake'] = validated_data.get('front_brake')
        # component_data['rear_brake'] = validated_data.get('rear_brake')

        # component_serializer = ProductComponentSerializer(data=component_data)
        # if component_serializer.is_valid(raise_exception=True):
        #     component_serializer.save()

    # def create(self, validated_data):        
    #     # 'body_id', 'battery_id', 'dimension_id', 'performance_id'
    #     product_obj = Product.objects.create(
    #         name=validated_data.get('name'),
    #         body_id=body_data,
    #         battery_id=battery_data,
    #         dimension_id=dimension_data,
    #         performance_id=performance_data,
    #         category=validated_data.get('category'),
    #         production_year=validated_data.get('production_year'),
    #         price=validated_data.get('price')
    #     )

        # return product_obj


class CombinedSerializer(serializers.Serializer):
    product_body = ProductBodySerializer(many=True)
    product_dimension = ProductDimensionSerializer(many=True)
    product_battery = ProductBatterySerializer(many=True)
    product_performance = ProductPerformanceSerializer(many=True)
    product_component = ProductComponentSerializer(many=True)
    product = ProductSerializer(many=True)