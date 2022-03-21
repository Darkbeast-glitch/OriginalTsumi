from email.headerregistry import Address
from pyexpat import model
from statistics import mode
from django.db import models

# Create your models here.


class userinformations(models.Model):
    first_name = models.CharField(max_length=200, null=False,blank=False)
    last_name = models.CharField(max_length=200, null=False,blank=False)
    address = models.CharField(max_length=1000, null=False,blank=False)
    phone = models.IntegerField()
    gender = models.CharField(max_length=2)


    def __str__(self):
        return self.first_name



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