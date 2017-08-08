# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20170808_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='itemViews',
            field=models.IntegerField(null=True, verbose_name=b'\xe6\x9f\xa5\xe7\x9c\x8b\xe6\xac\xa1\xe6\x95\xb0', blank=True),
        ),
    ]
