from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

class RedditPostView(APIView):
    authentication_classes = []
    permission_classes = []
    
    def post(self, request):
        try:
            start_date = request.data.get("start_date")
            end_date = request.data.get("end_date")
            
            if not start_date or not end_date:
                return Response({
                    "status": "error",
                    "msg": "Start & End Dates are required to get Reddit Post Data."
                }, status=400)
                
            # Handle Reddit Post Fetch Logic Here
        
        except Exception as ex:
            return Response({
                "status": "error",
                "msg": str(ex)
            }, status=400)
