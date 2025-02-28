from django.http import JsonResponse
from django.shortcuts import render
from .models import User
from .serializers import RegisterSerializer , CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
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


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self , request):
        user = request.user
        serializer = RegisterSerializer(user)
        return Response(serializer.data)
    

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self , request):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"message": "تم تسجيل الخروج بنجاح"} , status = status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response({"error": "لا يمكن تسجيل الخروج"} , status = status.HTTP_400_BAD_REQUEST)