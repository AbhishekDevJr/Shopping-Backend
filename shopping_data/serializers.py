from rest_framework import serializers
from .models.Brand import Brand
from .models.Category import Category
from .models.Products import Products

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["name", "desc", "is_active", "is_deleted"]
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "desc", "is_active", "is_deleted"]
        
class ProductsViewSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)
    description = serializers.CharField(read_only=True)
    price = serializers.IntegerField(read_only=True)
    category = serializers.SerializerMethodField(read_only=True)
    brand = serializers.SerializerMethodField(read_only=True)
    color = serializers.CharField(read_only=True)
    product_image = serializers.SerializerMethodField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)
    is_deleted = serializers.BooleanField(read_only=True)
    
    def get_category(instance):
        if instance.category:
            return instance.category.name
        return "N/A"
    
    def get_brand(instance):
        if instance.brand:
            return instance.brand.name
        return "N/A"
    
    def get_product_image(instance):
        if instance.product_image:
            return instance.product_image
        return "N/A"
    
    class Meta:
        model = Products
        fields = ["name", "description", "price", "category", "brand", "color", "product_image", "is_active", "is_deleted"]