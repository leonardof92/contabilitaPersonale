# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-24 09:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contoPersonale', '0011_conto_saldo_attuale'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conto',
            name='saldo_attuale',
        ),
    ]