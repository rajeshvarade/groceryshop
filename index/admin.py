from django.contrib import admin
from .models import Product
from .models import Cart

# Register your models here.
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ["name","price","image","unit"]

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ["name","price","image","unit"]