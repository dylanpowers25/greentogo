# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-04 00:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_subscription_stripe_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='stripe_status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
