# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_variation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='sale_price',
            field=models.DecimalField(blank=True, max_digits=20, decimal_places=2, null=True),
        ),
    ]
