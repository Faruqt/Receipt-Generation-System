from django.urls import path
from . import views

app_name = 'pdf_receipt'

urlpatterns = [
    path('api/receipt/', views.ReceiptView.as_view(), name='receipt'),
]
