# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-09-12 18:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('basket', '0002_auto_20180912_1843'),
        ('voucher', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='vouchers',
            field=models.ManyToManyField(blank=True, to='voucher.Voucher', verbose_name='Vouchers'),
        ),
        migrations.AlterUniqueTogether(
            name='line',
            unique_together=set([('basket', 'line_reference')]),
        ),
    ]
