# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='myCode',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='password',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='score',
            field=models.IntegerField(null=True),
        ),
    ]
