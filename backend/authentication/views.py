from django.shortcuts import render
# from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status, permissions

#import model and model serializer
from .serializers import RegisterUserSerializer

class CreateUserView(GenericAPIView):
    serializer_class = RegisterUserSerializer
	#allow new users to sign up and access receipt endpoint
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format='json'):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

