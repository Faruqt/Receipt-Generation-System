from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def receipt_in_pdf(template_path, context):
	#retrieve template using the template path provided
	template = get_template(template_path)
	#render html using the context object content
	html = template.render(context)
	#initilize memory byte buffer 
	result = BytesIO()

	#create pdf using the pisaDocument module from the xhtml2pdf package
	#then write into the memory buffer "result" created above
	pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)

	#confirm that there is no error
	if not pdf.err:
		#then return the value of the memory buffer
		return HttpResponse(result.getvalue(), content_type='application/pdf')
	return None
