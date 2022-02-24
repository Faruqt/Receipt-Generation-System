from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#import model and model serializer
from .models import Receipt
from .serializers import ReceiptSerializer

#import settings for converting to pdf
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

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
			serializer.save()
			return Response(status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def render_pdf_view(request, pk):
    template_path = 'api/receipt-pdf.html'

    obj = get_object_or_404(Receipt, pk=pk)
    context = {'obj': obj}

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="receipt.pdf"'

    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
