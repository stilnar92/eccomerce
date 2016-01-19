# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20151202_2338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='default_category',
        ),
        migrations.AddField(
            model_name='product',
            name='default',
            field=models.ForeignKey(related_name='default_category', null=True, blank=True, to='products.Category'),
        ),
    ]
