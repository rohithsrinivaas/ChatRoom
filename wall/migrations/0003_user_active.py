# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-25 12:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0002_user_pass_word'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]