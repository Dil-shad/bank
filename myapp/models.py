from django.db import models

# Create your models here.
class BankDetail(models.Model):
    ifsc=models.CharField(max_length=11)
    bank_id=models.CharField(max_length=10)
    branch=models.CharField(max_length=200)
    address=models.CharField(max_length=300)
    city=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    bank_name=models.CharField(max_length=250)

    def __str__(self):
        return self.ifsc
    

    