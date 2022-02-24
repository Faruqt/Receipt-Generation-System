from django.db import models
from django.utils import timezone

# Create your models here.
class Receipt(models.Model):
	name = models.CharField(max_length=120)
	address = models.CharField(max_length=240)
	phone = models.CharField(max_length=20)
	total_amount = models.PositiveIntegerField()
	created = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) 

	def __str__(self):
		return str(self.name)

	class Meta:
		ordering = ('-created',)
