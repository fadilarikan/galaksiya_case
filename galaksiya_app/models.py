from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model


class Product(models.Model):
   prod_id = models.CharField(max_length=200)
   title = models.CharField(max_length=200)
   image_uri = models.TextField()
   productCategory = models.TextField()
   datePublished = models.DateTimeField(auto_now_add=True)
   color = models.CharField(max_length=200,default=False)
   size = models.TextField()
   price = models.CharField(max_length=100,default=False)
   discount = models.BooleanField(default=False)
   inStock = models.BooleanField(default=False)

   def __str__(self):
      return self.title





# Create your models here.
