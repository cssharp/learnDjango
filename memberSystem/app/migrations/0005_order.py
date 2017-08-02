# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20170802_0632'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('orderId', models.AutoField(serialize=False, primary_key=True)),
                ('userName', models.CharField(max_length=100, null=True, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d', blank=True)),
                ('mobile', models.CharField(max_length=11, verbose_name=b'\xe6\x89\x8b\xe6\x9c\xba\xe5\x8f\xb7')),
                ('url', models.CharField(max_length=1000, null=True, verbose_name=b'\xe7\xbd\x91\xe5\x9d\x80', blank=True)),
                ('desc', models.TextField(null=True, verbose_name=b'\xe5\xa4\x87\xe6\xb3\xa8')),
            ],
            options={
                'verbose_name': '\u8ba2\u5355',
                'verbose_name_plural': '\u8ba2\u5355',
            },
        ),
    ]
