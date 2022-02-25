import itertools 
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


#import model and model serializer
from .models import Receipt
from .serializers import ReceiptSerializer

#import settings for converting to pdf
from .utils import receipt_in_pdf
from io import BytesIO
from django.core.files import File

class ReceiptView(APIView):
	# permission_classes = (IsAuthenticated,)

	# get list of all receipt sets 
	def get(self, request):
		receipt = Receipt.objects.all()
		serializer = ReceiptSerializer(receipt, many=True)
		return Response(serializer.data)

	#create a new receipt set
	def post(self, request):
		pdfs = {}
		receipt_no = []
		serialized = ReceiptSerializer(data=request.data)
		#confirm that input is correct and accurate
		if serialized.is_valid():
			#get post data 
			obj = request.data
			#loop through post data and assign it to the receipt templates
			for p in range(1,11):
				template = 'api/template' + str(p) +'.html'

				# call function to convert html template to pdf and assign the result
				# to the pdf variables (e.g pdf1)
				pdfs["pdf" +str(p)] = create_pdf(obj, template, p)

				#create receipt titles in the format e.g 'receipt_1'
				receipt_no.append('receipt_' + str(p))

			new_serializer_data = serialized.data

			#loop through pdf list and receipt_no array
			# then assign save it to the respective object model
			for pdf, receipt in zip(pdfs, receipt_no):
				new_serializer_data[receipt] = pdfs[pdf]
			
			#re-serialize 'new_serializer_data' object
			serializer = ReceiptSerializer(data=new_serializer_data)

			#confirm data is still valid and then save
			if serializer.is_valid():
				serializer.save()
				return Response(status=status.HTTP_201_CREATED)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

		return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

def create_pdf(obj, template, p):
	template_path = template
	context = {'obj': obj}

	#call functiom in utils.py script to create a template with the arguments
	# 'path to the template' and 'context' 
	pdf = receipt_in_pdf(template_path, context)
	if pdf:
		#set file name in the format "name of user" + receipt number e.g 'John_receipt1.pdf'
		filename = obj['name']+'_receipt'+ str(p) + '.pdf'

		#call function to convert returned bytes object to file
		user_receipt = bytes_to_file (pdf, filename)

	#finally return the generated pdf file to receipt function above 
	return user_receipt

def bytes_to_file(pdf, filename):
	# use the imported File class to handle the returned bytes object 
	receipt_file = File(BytesIO(pdf.content))

	#append filename to file created with the File class
	the_receipt = File(receipt_file, filename)

	return the_receipt
