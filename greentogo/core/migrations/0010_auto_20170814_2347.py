# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-14 23:47
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20170814_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corporatecode',
            name='code',
            field=models.CharField(
                max_length=20,
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message=
                        'Code can only contain capitol letters and numbers with no spaces. Must be between 4 and 20 characters.',
                        regex='^[A-Z0-9]{4,20}$'
                    )
                ]
            ),
        ),
    ]
