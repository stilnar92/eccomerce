# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0007_cart_tax_percentage'),
        ('orders', '0004_useraddress'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('shipping_total_price', models.DecimalField(decimal_places=2, max_digits=50, default=5.99)),
                ('order_price', models.DecimalField(max_digits=50, decimal_places=2)),
                ('billing_address', models.ForeignKey(to='orders.UserAddress', related_name='billing_address')),
                ('cart', models.ForeignKey(to='carts.Cart')),
                ('shipping_address', models.ForeignKey(to='orders.UserAddress', related_name='shipping_address')),
                ('user', models.ForeignKey(to='orders.UserCheckout')),
            ],
        ),
    ]
