from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    fat = models.FloatField(default=0)
    protein = models.FloatField(default=0)
    carbohydrate = models.FloatField(default=0)
    energy = models.FloatField(default=0)
    desc = models.CharField(max_length=3000)
    pub_date = models.DateField()

    def __str__(self):
        return self.product_name