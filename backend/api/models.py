from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Receipt(models.Model):
	name = models.CharField(max_length=120)
	address = models.CharField(max_length=240)
	phone = models.CharField(max_length=20)
	total_amount = models.PositiveIntegerField()
	created = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) 

	def get_absolute_url(self):
		return reverse('reports:detail', kwargs={'pk': self.pk})

	def __str__(self):
		return str(self.name)

	class Meta:
		ordering = ('-created',)
