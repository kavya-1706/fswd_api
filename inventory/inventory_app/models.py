from django.db import models

class Product(models.Model):
    prod_name = models.CharField(max_length=100)
    prod_id = models.IntegerField(unique=True)
    prod_price = models.DecimalField(max_digits=10, decimal_places=2)
    prod_mfd = models.DateField()
    prod_quan= models.IntegerField()
    prod_supplier= models.CharField(max_length=100)

    def __str__(self):
        return self.prod_name
