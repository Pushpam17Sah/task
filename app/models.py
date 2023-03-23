from django.db import models

# Create your models here.



class SalesInvoice(models.Model):
    customer_name=models.CharField(max_length=50)
    phone=models.CharField(max_length=12)
    address=models.TextField()
    amount=models.IntegerField()
    discount_amount=models.IntegerField()
    tax_percent=models.CharField(max_length=4) 
    invoice_items=models.JSONField()  
    created_at=models.DateTimeField(auto_now=True,editable=False)

    def __str__(self) :
        return self.customer_name
    
class BackupFiles(models.Model):
    file=models.FileField(upload_to="file/")
    back_up_date=models.DateTimeField(auto_now=True,editable=False)
    number_of_rows=models.IntegerField()
    size_of_file=models.IntegerField()
    file_type=models.CharField(max_length=12)

    
