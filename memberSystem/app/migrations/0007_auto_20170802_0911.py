# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20170802_0907'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='createTime',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 2, 9, 7, 49, 976934, tzinfo=utc), verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='updateTime',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 2, 9, 7, 49, 976934, tzinfo=utc), verbose_name=b'\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4', auto_now=True),
            preserve_default=False,
        ),
    ]
