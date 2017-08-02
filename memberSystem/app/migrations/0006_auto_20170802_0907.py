# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='isConfirmReceipt',
            field=models.BooleanField(default=datetime.datetime(2017, 8, 2, 9, 7, 23, 200900, tzinfo=utc), verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x94\xb6\xe8\xb4\xa7'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='isPurchased',
            field=models.BooleanField(default=datetime.datetime(2017, 8, 2, 9, 7, 36, 40878, tzinfo=utc), verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe9\x87\x87\xe8\xb4\xad'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='isReceiveOrder',
            field=models.BooleanField(default=datetime.datetime(2017, 8, 2, 9, 7, 49, 976934, tzinfo=utc), verbose_name=b'\xe6\x98\xaf\xe5\x90\xa6\xe6\x8e\xa5\xe5\x8d\x95'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='desc',
            field=models.TextField(null=True, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8', blank=True),
        ),
    ]
