# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20170808_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='itemDesc',
            field=ckeditor.fields.RichTextField(verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe6\x8f\x8f\xe8\xbf\xb0'),
        ),
        migrations.AlterField(
            model_name='item',
            name='itemId',
            field=models.AutoField(serialize=False, verbose_name=b'\xe5\x95\x86\xe5\x93\x81ID', primary_key=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='memberId',
            field=models.AutoField(serialize=False, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7ID', primary_key=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='orderId',
            field=models.AutoField(serialize=False, verbose_name=b'\xe8\xae\xa2\xe5\x8d\x95ID', primary_key=True),
        ),
    ]
