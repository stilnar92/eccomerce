# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20151201_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='inventory',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
