from typing import Any
from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

class Shop(models.Model):
    class meta: 
        verbosename="فروشگاه"
    shopname = models.CharField(max_length=50,default=True)
    location = models.TextField(max_length=50)
    shopphonenumber = models.CharField(max_length=15, validators=[RegexValidator(regex=r'\d{10,14}', message='Enter a valid phone number')])
    image = models.ImageField(upload_to='shop_images/', null=True, blank=True)
    def __str__(self) :
        return self.shopname

class User(models.Model):
    class meta: 
        verbosename="کاربر"
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50,null=True)
    userphonenumber = models.CharField(max_length=15, validators=[RegexValidator(regex=r'\d{10,14}', message='Enter a valid phone number')])
    gmail = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    address = models.TextField(max_length=100)
    gender = models.CharField(max_length=10,null=True,blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    nationalcode = models.CharField(null=True,blank=True,max_length=10)

class Makeup(models.Model):
    class meta:    
        verbosename="لوازم ارایشی"
    shopname = models.ForeignKey(Shop,on_delete=models.CASCADE,max_length=100,default=True)
    productname = models.CharField(max_length=100)
    remained = models.CharField(max_length=3)
    price = models.CharField(max_length=3)
    maincategory = models.CharField(max_length=20)
    aboutproduct = models.TextField(max_length=350)
    brandname = models.CharField(max_length=40)
    expdate = models.DateField()


class Skincare(models.Model):
    class meta:
        verbosename="لوازم مراقبت پوستی"
    shopname = models.ForeignKey(Shop,on_delete=models.CASCADE,default=True)
    productname = models.CharField(max_length=100)
    remained = models.CharField(max_length=3)
    price = models.CharField(max_length=3)
    maincategory = models.CharField(max_length=20)
    aboutproduct = models.TextField(max_length=350)
    brandname = models.CharField(max_length=40)
    expdate = models.DateField()

class Digitalstuff(models.Model):
    class Meta:
        verbose_name = "لوازم برقی"
    shopname =models.ForeignKey(Shop,on_delete=models.CASCADE,default=True)
    productname = models.CharField(max_length=20)
    remained = models.CharField(max_length=3)
    price = models.CharField(max_length=7)
    maincategory = models.CharField(max_length=20)
    brandname = models.CharField(max_length=20)
    aboutproduct = models.TextField(max_length=350)
    manufacturing_country = models.CharField(max_length=20)
    warranty = models.IntegerField()
    
class Sell(models.Model):
    class Meta:
        verbose_name = "فروش"
    address = models.CharField(max_length=350)
    housenumber = models.IntegerField()
    postalcode = models.IntegerField()
    paymentmethod = models.CharField(max_length=1000)   
    sendingtime = models.CharField(max_length=1000)   
    receivername = models.CharField(max_length=25)
    

class  Comment(models.Model): 
    product = models.ForeignKey(Makeup,Digitalstuff,Skincare)
    name = models.CharField(max_length=20) 
    commenttext = models.TextField(max_length=250) 
    shopname =models.ForeignKey(Shop,on_delete=models.CASCADE,default="shop")
      

