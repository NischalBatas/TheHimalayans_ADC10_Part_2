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

class order(models.Model):
    order_id=models.TextField()
    order_name=models.DateField()
    products=models.ForeignKey(Product,on_delete=models.DO_NOTHING)

class transaction(models.Model):
    transaction_id=models.TextField()
    transaction_date=models.DateField()
    products=models.ManyToManyField(Product)

class invoice(models.Model):
    invoice_id=models.TextField()
    invoice_details=models.TextField()
    products=models.ForeignKey(Product,on_delete=models.DO_NOTHING)
