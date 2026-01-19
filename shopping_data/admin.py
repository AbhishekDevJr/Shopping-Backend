from django.contrib import admin
from .models.Brand import Brand
from .models.Products import Products
# Register your models here.

admin.site.register(Brand)
admin.site.register(Products)