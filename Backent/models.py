from django.db import models

# Create your models here.

class admindb(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(null=True,blank=True)
    Username = models.CharField(max_length=50, null=True, blank=True)
    Password=models.CharField(max_length=100,null=True,blank=True)
    Image=models.ImageField(upload_to="media",null=True,blank=True)

class categorydb(models.Model):
    Name=models.CharField(max_length=200, null=True, blank=True)
    Description=models.CharField(max_length=100, null=True, blank=True)
    Image=models.ImageField(upload_to="profile",null=True, blank=True)

class productdb(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Category = models.ForeignKey(categorydb, on_delete=models.SET_NULL, null=True, blank=True)
    Description = models.CharField(max_length=200, null=True, blank=True)
    Quantity=models.IntegerField(null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)
    Size = models.CharField(max_length=50, null=True, blank=True)
    Color = models.CharField(max_length=50, null=True, blank=True)
    Image=models.ImageField(upload_to="profile",null=True,blank=True)

class contactdb(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(null=True,blank=True)
    Subject=models.CharField(max_length=100,null=True,blank=True)
    Message=models.CharField(max_length=100,null=True,blank=True)

