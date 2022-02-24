from django.urls import path
from .views import receipt

app_name = 'api'

urlpatterns = [
    path('receipt', receipt, name='receipt'),
]
