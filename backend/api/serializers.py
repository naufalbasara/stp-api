from rest_framework import serializers
from .models import  Product, ProductBody, ProductDimension, ProductBattery, ProductPerformance, ProductComponent
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password')

# class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super(MyTokenObtainPairSerializer, cls).get_token(user)      
#         token['detail'] = 'success'
#         token['username'] = user.username
#         return token

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
    image_1 = serializers.ImageField(required=False)
    image_2 = serializers.ImageField(required=False)
    image_3 = serializers.ImageField(required=False)

    class Meta:
        model = Product
        fields = (
            'id', 'name', 'lastEditedBy', 'body_id', 'battery_id', 'dimension_id',
            'performance_id', 'component_id', 'image_1', 'image_2', 'image_3',
            'category', 'production_year', 'price')
        depth = 1


class CombinedSerializer(serializers.Serializer):
    product_body = ProductBodySerializer(many=True)
    product_dimension = ProductDimensionSerializer(many=True)
    product_battery = ProductBatterySerializer(many=True)
    product_performance = ProductPerformanceSerializer(many=True)
    product_component = ProductComponentSerializer(many=True)
    product = ProductSerializer(many=True)