from django.contrib import admin

# Register your models here.
from products.models import ProductCatagory, Product

admin.site.register(Product)
admin.site.register(ProductCatagory)