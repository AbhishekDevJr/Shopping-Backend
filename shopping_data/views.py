from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.serializers import Serializer
from .models.Brand import Brand
from .serializers import BrandSerializer

# Create your views here.

class BrandView(APIView):
    authentication_classes = []
    permission_classes = []
    
    def get(self, request, brand_id=None):
        try:
            if not brand_id:
                brand_qs = Brand.objects.filter(is_active=True, is_deleted=False)
                brand_de_seri = BrandSerializer(brand_qs, many=True)
                
                return Response({
                    "status": "success",
                    "msg": "Brand List Retrieved.",
                    "data": brand_de_seri.data
                }, status=200)
            
            brand_obj = Brand.objects.get(id=brand_id)
            brand_obj_de_seri = BrandSerializer(brand_obj, many=False)
            
            return Response({
                "status": "success",
                "msg": f"Brand data with ID {brand_id} retrieved.",
                "data": brand_obj_de_seri.data
            }, status=200)
            
        except Brand.DoesNotExist as ex:
            return Response({
                "status": "error",
                "msg": f"Brand data with ID {brand_id} does not exists.",
            }, status=400)
            
        except Brand.MultipleObjectsReturned as ex:
            return Response({
                "status": "error",
                "msg": f"Multiple Brand data with same ID {brand_id} found."
            }, status=400)
            
        except Exception as ex:
            return Response({
                "status": "error",
                "msg": str(ex)
            }, status=500)