from django.http import JsonResponse
from django.shortcuts import render
from .models import User
from .serializers import RegisterSerializer , CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.




class RegisterView(APIView):
    def post(self , request):
        serializer = RegisterSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "تم التسجيل بنجاح"} , status = status.HTTP_201_CREATED)
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer