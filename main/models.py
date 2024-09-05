from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    # Add optional attributes if needed, e.g., stock, category, etc.
    stock = models.IntegerField(default=0)
    category = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name
