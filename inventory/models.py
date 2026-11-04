from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    sku = models.CharField(max_length=30, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=0) 
    description= models.TextField(blank=True)

    def __str__(self):
        return f"{self.name}+{self.sku}"