from django.db import models
from Backent.models import productdb


# Create your models here.

class customerdb(models.Model):
    Username = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Password = models.CharField(max_length=100, null=True, blank=True)
    Confirmpassword = models.CharField(max_length=100, null=True, blank=True)

class cartdb(models.Model):
    Proname= models.CharField(max_length=50,null=True,blank=True)
    Category=models.CharField(max_length=100,null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)
    Quantity=models.IntegerField(null=True,blank=True)

class checkoutdb(models.Model):
    Name= models.CharField(max_length=50,null=True,blank=True)
    Email = models.EmailField(max_length=100, null=True, blank=True)
    Address = models.CharField(max_length=100, null=True, blank=True)
    Pincode = models.IntegerField(null=True,blank=True)
    Phone = models.CharField(null=True,blank=True)
    CardName= models.CharField(max_length=50,null=True,blank=True)
    CreditNo = models.CharField(null=True,blank=True)
    Expiration = models.CharField(max_length=100, null=True, blank=True)
    Cvv = models.IntegerField(null=True,blank=True)

class wishlistdb(models.Model):
    Customer = models.ForeignKey(customerdb, on_delete=models.CASCADE)
    Product = models.ForeignKey(productdb, on_delete=models.CASCADE)







