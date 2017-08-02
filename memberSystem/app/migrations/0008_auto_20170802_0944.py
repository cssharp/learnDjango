# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20170802_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='isConfirmReceipt',
            field=models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x94\xb6\xe8\xb4\xa7'),
        ),
        migrations.AlterField(
            model_name='order',
            name='isPurchased',
            field=models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe9\x87\x87\xe8\xb4\xad'),
        ),
        migrations.AlterField(
            model_name='order',
            name='isReceiveOrder',
            field=models.BooleanField(default=False, verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x8e\xa5\xe5\x8d\x95'),
        ),
    ]
