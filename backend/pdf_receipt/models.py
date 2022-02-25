from django.db import models
from django.utils import timezone

# Create your models here.
class Receipt(models.Model):
	name = models.CharField(max_length=120)
	address = models.CharField(max_length=240)
	phone = models.CharField(max_length=20)
	total_amount = models.PositiveIntegerField()
	created = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) 
	receipt_1 = models.FileField(upload_to='receipts', null=True, blank=True)
	receipt_2 = models.FileField(upload_to='receipts', null=True, blank=True)
	receipt_3 = models.FileField(upload_to='receipts', null=True, blank=True)
	receipt_4 = models.FileField(upload_to='receipts', null=True, blank=True)
	receipt_5 = models.FileField(upload_to='receipts', null=True, blank=True)
	receipt_6 = models.FileField(upload_to='receipts', null=True, blank=True)
	receipt_7 = models.FileField(upload_to='receipts', null=True, blank=True)
	receipt_8 = models.FileField(upload_to='receipts', null=True, blank=True)
	receipt_9 = models.FileField(upload_to='receipts', null=True, blank=True)
	receipt_10 = models.FileField(upload_to='receipts', null=True, blank=True)

	def __str__(self):
		return str(self.name)

	class Meta:
		ordering = ('-created',)
