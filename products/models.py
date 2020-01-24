from django.db import models

# Create your models here.

class Product(models.Model):
    product_image=models.ImageField(upload_to='images/',null=True)
    product_name=models.TextField()
    product_price=models.FloatField()
    product_category=models.TextField()

    def valid_product(self):
        return self.product_name!=""
    
    def valid_price(self):
        return self.product_price>0

    def valid_category(self):
        return self.product_category!=""

class Order(models.Model):
    order_id=models.TextField()
    order_name=models.TextField()
    products=models.ForeignKey(Product,on_delete=models.DO_NOTHING)

    def valid_id(self):
        return self.order_id!=""

    def valid_name(self):
        return self.order_name!=""

class Transaction(models.Model):
    transaction_id=models.TextField()
    transaction_date=models.DateField()
    products=models.ManyToManyField(Product)

    def valid_Tid(self):
        return self.transaction_id!=""

    def valid_date(self):
        return self.transaction_date!=""
    
  
        

class Invoice(models.Model):
    invoice_id=models.TextField()
    invoice_details=models.TextField()
    products=models.ForeignKey(Product,on_delete=models.DO_NOTHING)

    def valid_Invoice_id(self):
        return self.invoice_id!=""

    def valid_Invoice_details(self):
        return self.invoice_details!=""
    
    
    

