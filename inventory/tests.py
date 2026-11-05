from django.test import TestCase
from django.db import IntegrityError
from .models import Product
class ProductTestCase(TestCase):
    def test_duplicate_sku_rejects(self):
        new_product1=Product.objects.create(name="laptop",price="55000.00",sku= "LAP-001")
        with self.assertRaises(IntegrityError):
            Product.objects.create(name="oil", price="550.00", sku="LAP-001")