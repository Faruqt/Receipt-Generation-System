from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#import model and model serializer
from .models import Receipt
from .serializers import ReciptSerializer


# Create your views here.
@api_view(['POST'])
def receipt(request):
		print(type(request.data))
        # serializer = NoteSerializer(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
