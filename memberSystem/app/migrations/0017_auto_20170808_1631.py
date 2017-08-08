# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_item_itemviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='itemViews',
            field=models.IntegerField(default=0, verbose_name=b'\xe6\x9f\xa5\xe7\x9c\x8b\xe6\xac\xa1\xe6\x95\xb0', blank=True),
        ),
    ]
