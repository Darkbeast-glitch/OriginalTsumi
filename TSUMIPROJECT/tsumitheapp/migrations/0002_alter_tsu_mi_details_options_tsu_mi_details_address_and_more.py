# Generated by Django 4.0.3 on 2022-04-14 17:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tsumitheapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tsu_mi_details',
            options={'verbose_name': 'TsuMiDetail', 'verbose_name_plural': 'TsuMiDetails'},
        ),
        migrations.AddField(
            model_name='tsu_mi_details',
            name='address',
            field=models.CharField(default=django.utils.timezone.now, max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tsu_mi_details',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
    ]
