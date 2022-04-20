# Generated by Django 4.0.3 on 2022-04-01 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=15)),
                ('message', models.TextField(max_length=5000)),
            ],
            options={
                'verbose_name': 'Contact_form',
                'verbose_name_plural': 'Contact_forms',
            },
        ),
        migrations.CreateModel(
            name='Register_Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('confirm_pass', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Register_Account',
                'verbose_name_plural': 'Register_Accounts',
            },
        ),
        migrations.CreateModel(
            name='Tsu_MI_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('send_type', models.CharField(max_length=50)),
                ('category_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=13)),
                ('item_list', models.TextField(max_length=5000)),
                ('fulfilled', models.BooleanField(default=False)),
                ('status', models.IntegerField(choices=[(0, 'Pending'), (1, 'Fulfilled')], default=0)),
                ('ordered_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'TsuMiDetail',
                'verbose_name_plural': 'TsuMiDetials',
            },
        ),
        migrations.CreateModel(
            name='userinformations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=1000)),
                ('phone', models.IntegerField()),
                ('gender', models.CharField(max_length=2)),
            ],
            options={
                'verbose_name': 'userinformation',
                'verbose_name_plural': 'userinformations',
            },
        ),
    ]
