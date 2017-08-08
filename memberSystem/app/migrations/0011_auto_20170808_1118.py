# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20170808_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='itemPics',
            field=models.ImageField(upload_to=b'items', verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe5\x9b\xbe\xe7\x89\x87'),
        ),
        migrations.AlterModelTable(
            name='item',
            table='ImageStore',
        ),
    ]
