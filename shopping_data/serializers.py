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
    
    def get_category(self, instance):
        if instance.category:
            return instance.category.name
        return "N/A"
    
    def get_brand(self, instance):
        if instance.brand:
            return instance.brand.name
        return "N/A"
    
    def get_product_image(self, instance):
        if instance.product_image:
            return instance.product_image
        return "N/A"
    
    class Meta:
        model = Products
        fields = ["name", "description", "price", "category", "brand", "color", "product_image", "is_active", "is_deleted"]
        

class ProductsPostSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    description = serializers.CharField()
    price = serializers.IntegerField()
    color = serializers.CharField()
    brand = serializers.PrimaryKeyRelatedField(
        queryset = Brand.objects.all()
    )
    category = serializers.PrimaryKeyRelatedField(
        queryset = Category.objects.all()
    )
    product_image = serializers.ImageField(required=True, allow_null=False)
    is_active = serializers.BooleanField()
    is_deleted = serializers.BooleanField()
    
    class Meta:
        model = Products
        fields = ["name", "description", "price", "color", "brand", "category", "product_image", "is_active", "is_deleted"]
    
    def create(self, validated_data):
        name = validated_data["name"]
        description = validated_data["description"]
        price = validated_data["price"]
        color = validated_data["color"]
        brand = validated_data["brand"]
        category = validated_data["category"]
        product_image = validated_data["product_image"]
        is_active = validated_data["is_active"]
        is_deleted = validated_data["is_deleted"]
        
        return Products.objects.create(
            name=name,
            description=description,
            price=price,
            color=color,
            brand=brand,
            category=category,
            product_image=product_image,
            is_active=is_active,
            is_deleted=is_deleted
        )
        
class CartGetSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)
    total_quantity = serializers.IntegerField(read_only=True)
    total_value = serializers.DecimalField(read_only=True, decimal_places=2, max_digits=10)
    created_date = serializers.DateField(read_only=True)
    items = serializers.SerializerMethodField(read_only=True)
    
    def get_user(self, instance):
        return instance.user.username if instance.user else "N/A"
    
    def get_items(self, instance):
        cart_items = instance.cart_items.all()
        cart_details = []
        
        for item in cart_items:
            cart_details.append({
                "product_name": item.product.name if item.product else "N/A",
                "product_quantity": item.product_quantity,
                "product_total_value": item.total_value
            })
        
        return cart_details