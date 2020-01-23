from django.test import TestCase
from .models import Product
# Create your tests here.
class ModelTestCase(TestCase):

    def test_valid_product(self):
        p1=Product(product_name="Boots",product_price=1500,product_category="Samsung")
        self.assertTrue(p1.valid_product())
