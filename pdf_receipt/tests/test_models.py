from django.test import TestCase
from pdf_receipt.models import Receipt
from django.utils import timezone


class ReceiptTest(TestCase):
	def create_receipt(self, name="Faruq", address="Wano Kingdom", phone="012345", total_amount=2000):
		return Receipt.objects.create(name=name, address=address, phone=phone, total_amount=total_amount, created=timezone.now().strftime("%Y-%m-%d"))

	def test_user_post_details(self):
		r = self.create_receipt()
		self.assertTrue(isinstance(r, Receipt))
		self.assertEqual(r.name, "Faruq")
		self.assertEqual(r.address, "Wano Kingdom" )
		self.assertEqual(r.phone, "012345" )
		self.assertEqual(r.total_amount, 2000)


