# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20170802_0615'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='updateTime',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 2, 6, 32, 21, 783271, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='member',
            name='createTime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
