# Generated by Django 4.0.3 on 2022-05-23 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tsumitheapp', '0014_paymentfees_delivery_fee_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paymentfees',
            old_name='payment_charge',
            new_name='paystack_fee',
        ),
    ]
