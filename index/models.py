

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='media/products/')
    unit = models.CharField(max_length=50,default="Kg")


    def __str__(self):
        return str(self.name)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='media/products/')
    unit = models.CharField(max_length=50,default="Kg")




    
