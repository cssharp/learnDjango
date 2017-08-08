# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20170808_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='itemPic2',
            field=models.ImageField(upload_to=b'items', null=True, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe5\x9b\xbe\xe7\x89\x872', blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='itemPic3',
            field=models.ImageField(upload_to=b'items', null=True, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe5\x9b\xbe\xe7\x89\x873', blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='itemPic4',
            field=models.ImageField(upload_to=b'items', null=True, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe5\x9b\xbe\xe7\x89\x874', blank=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='itemPic5',
            field=models.ImageField(upload_to=b'items', null=True, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe5\x9b\xbe\xe7\x89\x875', blank=True),
        ),
    ]
