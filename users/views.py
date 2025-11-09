from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .models.CustomUser import CustomUser
from .serializers import CustomUserSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

# Create your views here.

class RegistrationView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    
    def post(self, request, *args, **kwargs):
        try:
            if not request.data:
                return Response({
                    "status": "error",
                    "msg": "User registration details not provided.",
                }, status=400)
                
            user_de_seri = CustomUserSerializer(data = request.data)
            
            if user_de_seri.is_valid():
                user_de_seri.save()
                # IMPLEMENT MAIL TRIGGER UPON SUCCESSFULL REGISTRATION
                return Response({
                    "status": "success",
                    "msg": f"User registered successfully with Username : {user_de_seri.data["username"]}",
                    "data": user_de_seri.data
                }, status=201)
                
                
            return Response({
                "status": "error",
                "msg": "Bad User Registration Payload."
            }, status=400)
        except Exception as ex:
            return Response({
                "status": "error",
                "msg": str(ex)
            }, status=500)
            
            
class LoginView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]
    
    def post(self, request, *args, **kwargs):
        try:
            username = request.data.get('username')
            password = request.data.get('password')
            
            if not username or not password:
                return Response({
                    "status": "error",
                    "msg": "Both Username & Password are required."
                }, status=400)
                
            user = authenticate(request=request, username=username, password=password)
            
            if user:
                token, created = Token.objects.get_or_create(user=user)
                
                return Response({
                    "status": "success",
                    "msg": "User authenticated successfully.",
                    "token": f"Token {token.key}",
                    "createdAt": created
                }, status=200)
                
            return Response({
                "status": "error",
                "msg": "Invalid User Credentials."
            }, status=401)
            
        except Exception as ex:
            return Response({
                "status": "error",
                "msg": str(ex)
            }, status=500)
            

class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        try:
            auth_token = request.headers.get('Authorization')
            if not auth_token or not auth_token.startswith('Token '):
                return Response({
                    "status": "error",
                    "msg": "Invalid Auth Token or Wrong Token Format."
                }, status=400)
                
            token_key = auth_token.split(' ')[1]
            token_obj = Token.objects.get(key=token_key).delete()
            return Response({
                "status": "success",
                "msg": "User successfully logged out."
            }, status=200)
            
        except Token.DoesNotExist as ex:
            return Response({
                "status": "error",
                "msg": f"No Auth Token stored for Auth Key {token_key}"
            }, status=400)
        
        except Token.MultipleObjectsReturned as ex:
            token_qs = Token.objects.filter(key=token_key).delete()
            return Response({
                "status": "error",
                "msg": f"Multiple Auth Token Objects found for Auth Token Key {token_key}. Please Login again."
            }, status=400)
        
        except Exception as ex:
            return Response({
                "status": "error",
                "msg": str(ex)
            }, status=500)