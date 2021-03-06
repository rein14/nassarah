# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-09-08 13:07
from __future__ import unicode_literals

import apps.bank.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BankTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=128)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True)),
                ('currency', models.CharField(blank=True, max_length=8, null=True)),
                ('reference', models.CharField(blank=True, default=apps.bank.models._make_uuid, max_length=100, unique=True)),
                ('confirmed', models.BooleanField(default=False)),
                ('date_confirmed', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-date_created',),
            },
        ),
    ]
