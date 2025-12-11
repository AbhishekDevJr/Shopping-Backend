from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.serializers import Serializer
from .models.Brand import Brand
from .models.Category import Category
from .models.Products import Products
from .serializers import BrandSerializer, CategorySerializer, ProductsViewSerializer

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

    def post(self, request, category_id):
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

    def patch(self, request, brand_id=None):
        try:
            brand_update_data = request.data
            
            if not brand_id or not brand_update_data:
                return Response({
                    "status": "error",
                    "msg": "Brand ID &/or Brand Update data required for Brand Record Update."
                }, status=400)
            
            brand_obj = Brand.objects.get(id=brand_id, is_active=True, is_deleted=False)
            
            brand_de_seri = BrandSerializer(brand_obj, brand_update_data, partial=True)
            
            if brand_de_seri.is_valid():
                brand_de_seri.save()
                return Response({
                    "status": "Success",
                    "msg": f"Brand record updated with ID {brand_id}"
                }, status=200)
                
            return Response({
                "status": "error",
                "msg": f"Unknown Error occured while updating Brand Data with ID {brand_id}"
            }, status=400)
                
        except Brand.DoesNotExist as ex:
            return Response({
                "status": "error",
                "msg": f"Brand record not found for ID {brand_id}"
            }, status=400)
            
        except Brand.MultipleObjectsReturned as ex:
            return Response({
                "status": "error",
                "msg": f"Multiple Brand records found with ID {brand_id}"
            }, status=400)
        
        except Exception as ex:
            return Response({
                "status": "error",
                "msg": str(ex)
            }, status=500)


class CategoryView(APIView):
    authentication_classes = []
    permission_classes = []
    
    def get(self, request, category_id=None):
        try:
            if not category_id:
                category_qs = Category.objects.filter(is_active=True, is_deleted=False)
                serialized_data = CategorySerializer(category_qs, many=True)
                
                return Response({
                    "status": "success",
                    "msg": "Category List data retrieved successfully.",
                    "data": serialized_data.data
                }, status=200)
                
            category_obj = Category.objects.get(is_active=True, is_deleted=False, id=category_id)
            serialized_data = CategorySerializer(category_obj, many=False)
            
            return Response({
                "status": "success",
                "msg": f"Category Detail data retrieved successfully for ID {category_id}",
                "data": serialized_data.data
            }, status=200)
            
        except Category.DoesNotExist as e:
            return Response({
                "status": "error",
                "msg": f"Category Data not found for ID {category_id}",
                "error_msg": f"{str(e)}"
            }, status=400)
            
        except Category.MultipleObjectsReturned as e:
            return Response({
                "status": "error",
                "msg": f"Multiple Category Data found for ID {category_id}",
                "error_msg": f"{str(e)}"
            }, status=400)
        
        except Exception as ex:
            return Response({
                "status": "error",
                "msg": str(ex)
            }, status=500)
            
    def post(self, request, category_id):
        try:
            if not request.data:
                return Response({
                    "status": "error",
                    "msg": "Invalid Request Payload."
                }, status=400)
                
            category_name = request.data.get("name")
            category_desc = request.data.get("desc")
            
            if not category_name or not category_desc:
                return Response({
                    "status": "error",
                    "msg": "Invalid Request Payload"
                }, status=400)
                
            category_obj = {
                "name": category_name,
                "desc": category_desc,
                "is_active": True,
                "is_deleted": False
            }
            
            deserialized_data = CategorySerializer(data=category_obj, many=False)
            
            if deserialized_data.is_valid():
                data = deserialized_data.save()
                
                return Response({
                    "status": "success",
                    "msg": f"Category record created with Name {data.name}"
                }, status=201)
                
            return Response({
                "status": "error",
                "msg": deserialized_data.errors
            }, status=400)
            
        except Exception as ex:
            return Response({
                "status": "error",
                "msg": str(ex)
            }, status=500)
            
    def patch(self, request, category_id=None):
        try:
            if not category_id or not request.data:
                return Response({
                    "status": "error",
                    "msg": "Category ID & Category Data is required to Update."
                }, status=400)
                
            category_obj = Category.objects.get(is_active=True, is_deleted=False, id=category_id)
            deserialized_data = CategorySerializer(category_obj, request.data, partial=True)
            
            if deserialized_data.is_valid():
                data = deserialized_data.save()
                return Response({
                    "status": "success",
                    "msg": f"Category Data updated for Name {data.name}"
                }, status=200)
                
            return Response({
                "status": "error",
                "msg": deserialized_data.errors
            }, status=400)
                
        except Exception as ex:
            return Response({
                "status": "error",
                "msg": str(ex)
            }, status=500)
            
    def delete(self, request, category_id=None):
        try:
            if not category_id:
                return Response({
                    "status": "error",
                    "msg": "Category ID is required to delete Category Data."
                }, status=400)
                
            category_obj = Category.objects.get(id=category_id, is_active=True, is_deleted=False)
            category_obj.is_active = False
            category_obj.is_deleted = True
            category_obj.save()
            
            return Response({
                "status": "success",
                "msg": f"Successfully deleted Category record with ID {category_id}."
            }, status=200)
            
        except Category.DoesNotExist as ex:
            return Response({
                "status": "error",
                "msg": str(ex)
            }, status=400)
        
        except Category.MultipleObjectsReturned as ex:
            return Response({
                "status": "error",
                "msg": str(ex)
            }, status=400)
            
        except Exception as ex:
            return Response({
                "status": "error",
                "msg": str(ex)
            }, status=500)
            
            
class ProductView(APIView):
    authentication_classes = []
    permission_classes = []
    
    def get(self, request, product_id):
        try:
            if not product_id:
                product_qs = Products.objects.filter(is_active=True, is_deleted=False)
                product_serialized = ProductsViewSerializer(product_qs, many=True)
                
                return Response({
                    "status": "success",
                    "msg": "Successfully retrieved Product List.",
                    "data": product_serialized.data
                }, status=200)
                
            product_obj = Products.objects.get(is_active=True, is_deleted=False, id=product_id)
            product_obj_serialized = ProductsViewSerializer(product_obj, many=False)
            
            return Response({
                "status": "success",
                "msg": f"Successfully retrieved Product data for product ID: {product_id}",
                "data": product_obj_serialized.data
            }, status=200)
            
        except Products.DoesNotExist as ex:
            return Response({
                "status": "error",
                "msg": str(ex)
            }, status=400)
            
        except Products.MultipleObjectsReturned as ex:
            return Response({
                "status": "error",
                "msg": str(ex)
            }, status=400)
        
        except Exception as ex:
            return Response({
                "status": "error",
                "msg": str(ex)
            }, status=400)
            
    