from rest_framework import serializers
from .models.Brand import Brand

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["name", "desc", "is_active", "is_deleted"]