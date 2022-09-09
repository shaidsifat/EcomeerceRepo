from django.contrib import admin

# Register your models here.
from product.models import product,Order
admin.site.register(product) 
admin.site.register(Order)