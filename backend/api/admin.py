from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductBody)
admin.site.register(ProductDimension)
admin.site.register(ProductBattery)
admin.site.register(ProductPerformance)
admin.site.register(ProductComponent)