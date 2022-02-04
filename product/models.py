from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=255, blank=False, null=False)
    weight = models.FloatField(blank=False, null=False)
    price = models.FloatField(blank=False, null=False)
    created_at = models.DateField(blank=False, null=False)
    updated_at = models.DateField(blank=False)
    class Meta:
        db_table='product_db'

    def __str__(self):
        return self.name
