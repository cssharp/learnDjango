# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20170802_0944'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.IntegerField(null=True, verbose_name=b'\xe4\xbb\xb7\xe6\xa0\xbc\xe7\xbe\x8e\xe5\x85\x83($)', blank=True),
        ),
    ]
