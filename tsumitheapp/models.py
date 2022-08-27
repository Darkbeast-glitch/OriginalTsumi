from email.headerregistry import Address
from enum import Flag
from operator import mod
from pyexpat import model
import secrets
from statistics import mode
from tabnanny import verbose
from unicodedata import digit
from xmlrpc.client import TRANSPORT_ERROR
from django.db import models
from .paystack import Paystack
from random import choices, randint, randrange


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


class Popular_Details(models.Model):
    card_title = models.CharField(max_length=100, blank=False, null=False)
    card_price = models.CharField(max_length=100, blank=False, null=False)
    card_img = models.URLField(max_length = 200000)



    def __str__(self):
        return self.card_title

    class Meta:
        verbose_name = 'Popular Detail'
        verbose_name_plural = 'Popular Details'



class Payment(models.Model):
    fullname=models.CharField(max_length=200,blank=False, null=False)
    
    amount = models.PositiveIntegerField()
    ref = models.CharField(max_length=200)
    email = models.EmailField()
    verified = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    

    class Meta:
        ordering = ('-date_created',)

    def __str__(self)-> str:
        return f"Payment:{self.amount}"

    def save(self,*args,**kwargs) -> None:
        while not self.ref:
            ref =  "TM" + str(randrange(100000, 1000000))
            object_with_similar_ref= Payment.objects.filter(ref=ref)
            if not object_with_similar_ref:
                self.ref = ref
        super().save(*args,**kwargs)


    def amount_value(self) -> int:
        return self.amount *100

    def verify_payment(self):
        paystack = Paystack()
        status, result = paystack.verify_payment(self.ref,self.amount)
        if status:
            if result['amount']/100 == self.amount:
                self.verified = True

            self.save()
        if self.verified:
            return True
        return False




class PaymentFees(models.Model):
    DELIVERY_AREA = [

        ('Accra', 'Accra'),
        ('Kasoa', 'Kasoa'),
        ('Tema','Tema'),
        ('Kumasi', 'Kumasi'),
        ('Eastern', 'Eastern'),
    ]
    DELIVERY_FEE = [

        ('Accra', '20'),
        ('Kasoa', '30'),
        ('Tema', '20'),
        ('Kumasi', '100'),
    ]
    paystack_fee = models.IntegerField()
    elevy = models.CharField(max_length=10)
    Delivery_area = models.CharField(max_length=200, choices=DELIVERY_AREA)
    Delivery_fee = models.IntegerField()


    

    def __str__(self):
        return self.Delivery_area

    class Meta:
        verbose_name = 'PaymentFee'
        verbose_name_plural = 'PaymentFees'
