from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    price = models.FloatField()
    discount = models.IntegerField(default=0)
    short_desc = models.TextField()
    description = models.TextField()

    image = models.CharField(max_length=255)

    def __str__(self):
        return self.product_name