# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-09-13 15:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billingaddress',
            name='line3',
        ),
        migrations.RemoveField(
            model_name='billingaddress',
            name='postcode',
        ),
        migrations.RemoveField(
            model_name='billingaddress',
            name='state',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='line3',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='notes',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='postcode',
        ),
        migrations.RemoveField(
            model_name='shippingaddress',
            name='state',
        ),
        migrations.AlterField(
            model_name='billingaddress',
            name='line1',
            field=models.CharField(max_length=255, verbose_name='First address option'),
        ),
        migrations.AlterField(
            model_name='billingaddress',
            name='line2',
            field=models.CharField(blank=True, help_text='In case we dont catch with you at first address', max_length=255, verbose_name='Second address option'),
        ),
        migrations.AlterField(
            model_name='billingaddress',
            name='line4',
            field=models.CharField(blank=True, choices=[('Accra', 'Accra'), ('Kumasi', 'Kumasi'), ('Tema', 'Tema'), ('Koforidua', 'Koforidua'), ('Cape-Coast', 'Cape-Coast'), ('Takoradi', 'Takoradi'), ('Sunyani', 'Sunyani'), ('Tamale', 'Tamale'), ('Ho', 'Ho'), ('Bolgatanga', 'Bolgatanga'), ('Wa', 'Wa')], max_length=255, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='line1',
            field=models.CharField(max_length=255, verbose_name='First address option'),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='line2',
            field=models.CharField(blank=True, help_text='In case we dont catch with you at first address', max_length=255, verbose_name='Second address option'),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='line4',
            field=models.CharField(blank=True, choices=[('Accra', 'Accra'), ('Kumasi', 'Kumasi'), ('Tema', 'Tema'), ('Koforidua', 'Koforidua'), ('Cape-Coast', 'Cape-Coast'), ('Takoradi', 'Takoradi'), ('Sunyani', 'Sunyani'), ('Tamale', 'Tamale'), ('Ho', 'Ho'), ('Bolgatanga', 'Bolgatanga'), ('Wa', 'Wa')], max_length=255, verbose_name='City'),
        ),
    ]
