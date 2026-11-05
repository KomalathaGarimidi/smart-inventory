from django.contrib import admin

# Register your models here.
from .models import Product

#Basic registration
# admin.site.register(Product)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','sku','created_at','quantity','description')
