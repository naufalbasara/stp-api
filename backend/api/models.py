from django.db import models
import datetime as date

# Create your models here.
class User(models.Model):
    name = models.TextField(max_length=45)
    username = models.TextField(max_length=15)

class ProductBody(models.Model):
    product_class = models.TextField(max_length=45)
    style = models.TextField(max_length=45)
    layout = models.TextField(max_length=45)
    frame = models.TextField(max_length=45)

class ProductDimension(models.Model):
    length = models.DecimalField(decimal_places=2, max_digits=6)
    width = models.DecimalField(decimal_places=2, max_digits=6)
    height = models.DecimalField(decimal_places=2, max_digits=6)
    wheelbase = models.DecimalField(decimal_places=2, max_digits=6)
    weight = models.DecimalField(decimal_places=2, max_digits=6)

class ProductBattery(models.Model):
    battery_capacity = models.TextField(max_length=45)
    charge_port = models.TextField(max_length=45)
    port_location = models.TextField(max_length=45)
    voltage = models.TextField(max_length=45)
    charging_time = models.TextField(max_length=45)

class ProductPerformance(models.Model):
    top_speed = models.IntegerField()
    electric_range = models.IntegerField()
    power = models.TextField(max_length=45)
    torque = models.IntegerField()
    drivetrain = models.TextField(max_length=45)

class ProductComponent(models.Model):
    rim = models.TextField(max_length=45)
    front_tire = models.TextField(max_length=45)
    rear_tire = models.TextField(max_length=45)
    front_suspension = models.TextField(max_length=45)
    rear_suspension = models.TextField(max_length=45)
    front_brake = models.TextField(max_length=45)
    rear_brake = models.TextField(max_length=45)

class Product(models.Model):
    name = models.TextField(max_length=45)
    lastEditedBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    body_id = models.ForeignKey(ProductBody, on_delete=models.CASCADE, null=True)
    battery_id = models.ForeignKey(ProductBattery, on_delete=models.CASCADE, null=True)
    dimension_id = models.ForeignKey(ProductDimension, on_delete=models.CASCADE, null=True)
    performance_id = models.ForeignKey(ProductPerformance, on_delete=models.CASCADE, null=True)
    category = models.TextField(max_length=45, null=True)
    production_year = models.DateField(null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0.0)