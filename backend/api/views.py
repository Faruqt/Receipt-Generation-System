from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#import model and model serializer
from .models import Receipt
from .serializers import ReceiptSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def receipt(request):
	if request.method == 'GET':
		receipt = Receipt.objects.all()
		serializer = ReceiptSerializer(receipt, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		print(request.data)
		serializer = ReceiptSerializer(data=request.data)
		if serializer.is_valid():
			print(serializer)
        #     serializer.save()
        #     return Response(status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
