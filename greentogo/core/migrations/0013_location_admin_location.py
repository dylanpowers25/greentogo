# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-02-15 16:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_merge_20170814_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='admin_location',
            field=models.BooleanField(default=False, help_text='Admin locations are locations where         boxes will be checked in when resetting a         subscriptions box count manually'),
        ),
    ]
