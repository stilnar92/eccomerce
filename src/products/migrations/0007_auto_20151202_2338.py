# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20151202_2232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='default',
            new_name='default_category',
        ),
    ]
