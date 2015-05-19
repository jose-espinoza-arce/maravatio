# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_customimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='customimage',
            name='name',
            field=models.CharField(default='name', max_length=30),
            preserve_default=False,
        ),
    ]
