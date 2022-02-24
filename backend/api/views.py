from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#import model and model serializer
from .models import Receipt
from .serializers import ReceiptSerializer

#import settings for converting to pdf
from .utils import render_to_pdf
from io import BytesIO
from django.core.files import File

# Create your views here.
@api_view(['GET', 'POST'])
def receipt(request):
	if request.method == 'GET':
		receipt = Receipt.objects.all()
		serializer = ReceiptSerializer(receipt, many=True)
		return Response(serializer.data)

	elif request.method == 'POST':
		serialized = ReceiptSerializer(data=request.data)
		if serialized.is_valid():
			# print(serializer)
			obj = request.data
			pdf = create_pdf(obj)
			new_serializer_data = serialized.data
			new_serializer_data['receipt'] = pdf
			serializer = ReceiptSerializer(data=new_serializer_data)

			if serializer.is_valid():
				serializer.save()
				return Response(status=status.HTTP_201_CREATED)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

def create_pdf(obj):
	template_path = 'api/receipt-pdf.html'
	css = 'static/css/style.css'

	context = {'obj': obj}
	pdf = render_to_pdf(template_path, context)
	if pdf:
		filename = 'receipt.pdf'
		receipt_file = File(BytesIO(pdf.content))
		user_receipt = File(receipt_file, filename)
	
	return user_receipt


