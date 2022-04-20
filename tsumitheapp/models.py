from email.headerregistry import Address
from enum import Flag
from pyexpat import model
from statistics import mode
from unicodedata import digit
from django.db import models

# Create your models here.


STATUS = (
    (0, "Pending"),
    (1, "Fulfilled")
)


class userinformations(models.Model):
    first_name = models.CharField(max_length=200, null=False,blank=False)
    last_name = models.CharField(max_length=200, null=False,blank=False)
    address = models.CharField(max_length=1000, null=False,blank=False)
    phone = models.IntegerField()
    gender = models.CharField(max_length=2)


    def __str__(self):
        return self.first_name
    class Meta:
        verbose_name = 'userinformation'
        verbose_name_plural = 'userinformations'



class Register_Account(models.Model):
    user = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    confirm_pass = models.CharField(max_length=100)

    def __str__(self):
        return self.lastname

    class Meta:
        verbose_name = 'Register_Account'
        verbose_name_plural = 'Register_Accounts'

class Contact_form(models.Model):
    fullname = models.CharField(max_length=100, null=False, blank=False)
    email = models.CharField(max_length=200,null=False, blank=False)
    phone = models.CharField(max_length=15,null=False, blank=False)
    message = models.TextField(max_length=5000)

    def __str__(self):
        return self.fullname

        
    class Meta:
        verbose_name = 'Contact_form'
        verbose_name_plural = 'Contact_forms'



class Tsu_MI_Details(models.Model):
    fullname = models.CharField(max_length=200, null=False, blank=False)
    city = models.CharField(max_length=50, null=False, blank=False)
    send_type = models.CharField(max_length=50, null=False, blank=False)
    category_name = models.CharField(max_length=100, null=False, blank=False)
    address = models.CharField(max_length=500, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    item_list = models.TextField(max_length=5000)
    fulfilled = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS, default=0)
    ordered_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = 'TsuMiDetail'
        verbose_name_plural = 'TsuMiDetails'