from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import CustomUserSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.

class SignupApiView(APIView):
    permission_classes = [AllowAny]  

    def post(self, request):
        serializers = CustomUserSerializer(data=request.data)
        if serializers.is_valid():
            user = serializers.save()
            return Response({'message': 'User is created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class loginApiView(APIView):

    permission_classes = [AllowAny] 

    def post(self, request):
        print("lllllllllllllllllll")
        email = request.data.get('email')
        password = request.data.get('password')
        print(email, password)

        user = authenticate(email=email, password=password)
        print(user)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            access = refresh.access_token
            response_data = {
                'refresh': str(refresh),
                'access': str(access),
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



