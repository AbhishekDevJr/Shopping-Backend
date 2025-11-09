from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models.CustomUser import CustomUser

class CustomUserSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        
    def create(self, validated_data):
        user = CustomUser(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user
    
    # IMPLEMENT UPDATE FUNC HERE IF REQUIRED