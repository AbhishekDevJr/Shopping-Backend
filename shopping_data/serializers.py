from rest_framework import serializers
from .models.Brand import Brand
from .models.Category import Category

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["name", "desc", "is_active", "is_deleted"]
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "desc", "is_active", "is_deleted"]