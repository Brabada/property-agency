# Generated by Django 2.2.24 on 2022-12-20 22:23

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20221211_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='owner_pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=20, null=True, region='RU', verbose_name='Нормализованный номер владельца'),
        ),
    ]
