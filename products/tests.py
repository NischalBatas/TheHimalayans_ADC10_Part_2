from django.test import TestCase
from .models import Product, Order, Transaction, Invoice
# Create your tests here.
class ModelTestCase(TestCase):

    #Product class testing
    def test_valid_product(self):
        p1=Product(product_name="Boots",product_price=1500,product_category="Samsung")
        self.assertTrue(p1.valid_product())

    def test_valid_price(self):
        price1=Product(product_price=15000.0)
        self.assertEqual(price1.valid_price(), True)

    def test_valid_category(self):
        category1=Product(product_category="Mobile")
        self.assertTrue(category1.valid_category())

    #Order class testing
    def test_valid_id(self):
        id1=Order(order_id="S101")
        self.assertTrue(id1.valid_id())

    def test_valid_name(self):
        name1=Order(order_name="Samsung A20")
        self.assertEqual(name1.valid_name(),True)

    #Transaction class testing
    def test_valid_Tid(self):
        tran1=Transaction(transaction_id="T01")
        self.assertEqual(tran1.valid_Tid(),True)

    def test_valid_date(self):
        date1=Transaction(transaction_date=2020/1/10)
        self.assertEqual(date1.valid_date(),True)

    #Invoice class testing
    def test_valid_Invoice_id(self):
        id1=Invoice(invoice_id="I101")
        self.assertEqual(id1.valid_Invoice_id(), True)

    def test_valid_Invoice_details(self):
        details1=Invoice(invoice_details="The product details")
        self.assertEqual(details1.valid_Invoice_details(),True)

    