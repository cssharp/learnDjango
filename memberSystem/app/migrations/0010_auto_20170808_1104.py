# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_order_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('itemId', models.AutoField(serialize=False, primary_key=True)),
                ('itemName', models.CharField(max_length=100, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe5\x90\x8d\xe7\xa7\xb0')),
                ('itemPics', models.CharField(max_length=500, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe5\x9b\xbe\xe7\x89\x87')),
                ('itemUSDPrice', models.IntegerField(null=True, verbose_name=b'\xe4\xbb\xb7\xe6\xa0\xbc\xe7\xbe\x8e\xe5\x85\x83($)', blank=True)),
                ('itemCnPrice', models.IntegerField(null=True, verbose_name=b'\xe4\xbb\xb7\xe6\xa0\xbc\xe4\xba\xba\xe6\xb0\x91\xe5\xb8\x81(\xc2\xa5)', blank=True)),
                ('itemDesc', models.TextField(max_length=500, verbose_name=b'\xe5\x95\x86\xe5\x93\x81\xe6\x8f\x8f\xe8\xbf\xb0')),
                ('itemWeight', models.IntegerField(verbose_name=b'\xe9\x87\x8d\xe9\x87\x8f\xef\xbc\x88\xe7\xa3\x85\xef\xbc\x89')),
                ('itemSourceUrl', models.CharField(max_length=300, null=True, verbose_name=b'\xe5\x95\x86\xe5\x93\x81url', blank=True)),
            ],
            options={
                'verbose_name': '\u5546\u54c1',
                'verbose_name_plural': '\u5546\u54c1\u5217\u8868',
            },
        ),
        migrations.AlterModelOptions(
            name='member',
            options={'verbose_name': '\u7528\u6237', 'verbose_name_plural': '\u7528\u6237\u5217\u8868'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': '\u8ba2\u5355', 'verbose_name_plural': '\u8ba2\u5355\u5217\u8868'},
        ),
    ]
