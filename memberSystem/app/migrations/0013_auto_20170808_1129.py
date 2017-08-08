# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20170808_1127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='itemPics',
        ),
        migrations.AddField(
            model_name='item',
            name='itemPic1',
            field=models.ImageField(default=1, upload_to=b'items', verbose_name=b'\xe4\xb8\xbb\xe5\x9b\xbe'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='itemPic2',
            field=models.ImageField(default=1, upload_to=b'items', verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe5\x9b\xbe\xe7\x89\x872'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='itemPic3',
            field=models.ImageField(default=1, upload_to=b'items', verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe5\x9b\xbe\xe7\x89\x873'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='itemPic4',
            field=models.ImageField(default=1, upload_to=b'items', verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe5\x9b\xbe\xe7\x89\x874'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='itemPic5',
            field=models.ImageField(default=1, upload_to=b'items', verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe5\x9b\xbe\xe7\x89\x875'),
            preserve_default=False,
        ),
    ]
