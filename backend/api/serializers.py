from rest_framework import serializers
from .models import Receipt

class ReciptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = ('id', 'name', 'address', 'phone', 'total_amount')

