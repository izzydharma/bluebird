from django.db import models
from django.utils import timezone

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)  # for ratings like 4.5
    date = models.IntegerField()  # auto-populates with the current date

    def __str__(self):
        return self.name
