from django.db import models
from datetime import date
from django.contrib.auth.models import User
from myadmin.models import *



class Customer_inquiry(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    contact = models.BigIntegerField()
    message = models.TextField()
    date = models.DateField(default=date.today)

    class Meta:
        db_table = 'cust_inquiry'
#--------------------------------------------------------------------
class Customer_feedback(models.Model):
    rating = models.CharField(max_length=20,null=True)
    message = models.TextField()

    date = models.DateField(default=date.today)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    class Meta:
        db_table = 'cust_feedback'
#--------------------------------------------------------------------
class Profile(models.Model):
    address = models.TextField()
    gender = models.CharField(max_length=30)
    contact = models.BigIntegerField()
    reg_date = models.DateField(default=date.today)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_image=models.CharField(max_length=255,null=True)

    class Meta:
        db_table = 'profile'
#--------------------------------------------------------------------
class Upload_product(models.Model):
    productname = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    price = models.BigIntegerField()
    description = models.CharField(max_length=200,null=True)
    largedes = models.TextField(null=True)
    image = models.CharField(max_length=250)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory,on_delete=models.CASCADE,null=True)
    contact = models.BigIntegerField(null=True)
    date = models.DateField(default=date.today,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default='')

    class Meta:
        db_table = 'upload_product'
#--------------------------------------------------------------------
class Cart_store(models.Model):
    productname = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    price = models.BigIntegerField()
    description = models.CharField(max_length=200,null=True)
    largedes = models.TextField(null=True)
    image = models.CharField(max_length=250)
    uploader = models.ForeignKey(Upload_product,on_delete=models.CASCADE,default='')
    cart_date = models.DateField(default=date.today,null=True)
    sellercontact = models.BigIntegerField(null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default='')

    class Meta:
        db_table = 'cart'



class password_all(models.Model):
    user_password  = models.CharField(max_length=30)
    user = models.ForeignKey(User,on_delete=models.CASCADE,default='')
#--------------------------------------------------------------------
