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
                    "data": brand_de_seri.data,
                    "count": len(brand_de_seri.data)
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
            
            
    def post(self, request):
        try:
            brand_data = request.data
            
            if not brand_data:
                return Response({
                    "status": "error",
                    "msg": "Brand data required to Create Brand Record."
                }, status=400)
                
            brand_name = brand_data.get("brand_name", None)
            brand_desc = brand_data.get("brand_desc", None)
            
            brand_obj = {
                "name": brand_name,
                "desc": brand_desc,
                "is_active": True,
                "is_deleted": False
            }
            
            brand_de_seri = BrandSerializer(data=brand_obj, many=False)
            
            if brand_de_seri.is_valid():
                brand_de_seri.save()
                
                return Response({
                    "status": "success",
                    "msg": f"Brand record successfully created with Brand Name: {brand_de_seri.data["name"]}"
                }, status=201)
                
            else:
                return Response({
                    "status": "error",
                    "msg": "Incorrect Brand data. Brand Name should be Unique.",
                }, status=400)
            
        except Exception as ex:
            return Response({
                "status": "error",
                "msg": str(ex)
            }, status=500)
            
    def delete(self, request, brand_id=None):
        try:
            if not brand_id:
                return Response({
                    "status": "error",
                    "msg": "Brand ID is required to Delete Brand Record."
                }, status=400)
                
            brand_obj = Brand.objects.get(id=brand_id, is_active=True, is_deleted=False)
            brand_obj.is_active=False
            brand_obj.is_deleted=True
            brand_obj.save()
            
            return Response({
                "status": "success",
                "msg": f"Brand record with ID: {brand_id} successfully deleted."
            }, status=200)
            
        except Brand.DoesNotExist as ex:
            return Response({
                "status": "error",
                "msg": f"No Brand Record exists or Brand record already deleted with ID: {brand_id}"
            }, stutus=400)
            
        except Brand.MultipleObjectsReturned as ex:
            return Response({
                "status": "error",
                "msg": f"Multiple Brand records found with ID: {brand_id}"
            }, status=400)
                
        except Exception as ex:
            return Response({
                "status": "error",
                "msg": str(ex)
            }, status=500)