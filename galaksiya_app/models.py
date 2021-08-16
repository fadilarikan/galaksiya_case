from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model


class Product(models.Model):
   prod_id = models.CharField(max_length=200)
   title = models.CharField(max_length=200)
   image_uri = models.TextField()
   productCategory = models.TextField()
   datePublished = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return self.title





# Create your models here.
