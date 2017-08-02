# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('memberId', models.AutoField(serialize=False, primary_key=True)),
                ('email', models.CharField(max_length=50)),
                ('userName', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('score', models.IntegerField()),
                ('isDeleted', models.BooleanField()),
                ('isEnabled', models.BooleanField()),
                ('createTime', models.DateTimeField()),
                ('myCode', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': '\u7528\u6237',
                'verbose_name_plural': '\u7528\u6237',
            },
        ),
    ]
